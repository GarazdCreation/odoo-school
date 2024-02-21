from odoo import _, api, fields, models
from odoo.exceptions import UserError


class SocialSubscriber(models.Model):
    _inherit = 'social.subscriber'

    @api.model
    def default_get(self, fields_list):
        default_vals = super(SocialSubscriber, self).default_get(fields_list)
        # Set a sequence to place a new record to the end
        max_sequence = self.env['social.subscriber'].search([], order='sequence DESC', limit=1).sequence or 0
        default_vals['sequence'] = max_sequence + 1
        return default_vals

    @api.returns('res.country')
    def _get_allowed_country(self):
        return self.env.ref('base.us') + self.env.ref('base.ua') + self.env.ref('base.ca')

    nickname = fields.Char(copy=False)

    # New approach to get a record name (instead of "name_get" method)
    @api.depends('name', 'nickname')
    def _compute_display_name(self):
        for rec in self:
            rec.display_name = "%s (%s)" % (rec.name, rec.nickname or '')

    @api.onchange('nickname')
    def _onchange_nickname(self):
        """ Set a social service as undefined if a subscriber nickname is not specified. """
        if not self.nickname:
            self.social_service = 'undefined'

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            # If a subscriber nickname is known, we will mark this subscriber as confirmed (+ add bonus)
            if vals.get('nickname'):
                vals.update({
                    'is_confirmed': True,
                    'client_bonus': vals.get('client_bonus', 0) + 100.0,
                })
            # Check the "bank_id" param
            if 'bank_id' in vals:
                bank = self.env['res.bank'].browse(vals['bank_id'])
                # Do some actions with this bank record
        return super(SocialSubscriber, self).create(vals_list)

    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        self.ensure_one()
        default = dict(default or {})
        # Add the suffix "(Copy)" to a subscriber name
        if 'name' not in default:
            default['name'] = _("%s (Copy)", self.name)
        # Set the state "new" for a subscriber copy
        default['state'] = 'new'
        return super(SocialSubscriber, self).copy(default=default)

    @api.ondelete(at_uninstall=False)
    def _unlink_except_facebook(self):
        for subscriber in self:
            if subscriber.social_service == 'facebook':
                raise UserError(_('You cannot remove a subscriber of your Facebook account.'))

    def write(self, vals):
        """ If a subscriber nickname is added or removed, change the "is_confirmed" field value.
            1) If it's added, we will mark this subscriber as confirmed.
            2) If it's removed, we will mark this subscriber as unconfirmed.
        """
        if 'nickname' in vals:
            vals['is_confirmed'] = bool(vals.get('nickname'))
        return super(SocialSubscriber, self).write(vals)

    def unlink(self):
        """ Archive subscribers that have a client bonus, instead of deleting them."""
        subscriber_with_bonus = self.filtered('client_bonus')
        subscriber_with_bonus.write({'active': False})
        return super(SocialSubscriber, self - subscriber_with_bonus).unlink()

