from odoo import _, api, models
from odoo.exceptions import UserError, ValidationError


class SocialPromo(models.Model):
    _inherit = 'social.promo'

    @api.constrains('name', 'subscriber_id')
    def _check_name_unique(self):
        for rec in self:
            if self.search_count([
                ('name', '=', rec.name),
                ('subscriber_id', '=', rec.subscriber_id.id),
            ]) > 1:
                raise ValidationError(
                    _('The name of a promotion must be unique per subscriber.')
                )

    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        """ Restrict a promotion duplicating. """
        # pylint: disable-msg=method-required-super
        raise UserError(_('You cannot duplicate a social promotion.'))
