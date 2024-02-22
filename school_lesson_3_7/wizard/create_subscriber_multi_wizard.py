# Copyright © 2024 Garazd Creation (https://garazd.biz)
# @author: Yurii Razumovskyi (support@garazd.biz)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.html).

from odoo import _, fields, models


class CreateSubscriberMultiWizard(models.TransientModel):
    _name = 'create.subscriber.multi.wizard'
    _description = "Wizard to create subscribers in the fast way."

    names = fields.Char(
        string='Subscriber Names',
        help='Specify subscriber names divided by comma.',
        required=True,
    )
    social_service = fields.Selection(
        selection=[
            ('undefined', 'Undefined'),
            ('instagram', 'Instagram'),
            ('tiktok', 'TikTok'),
            ('youtube', 'YouTube'),
            ('facebook', 'Facebook'),
        ],
    )
    country_id = fields.Many2one(comodel_name='res.country')

    def action_open_wizard(self):
        return {
            'name': _('Create Subscriber Wizard'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'create.subscriber.multi.wizard',
            'target': 'new',
            'context': {'default_country_id': self.env.user.country_id.id},
        }

    def action_create(self):
        self.ensure_one()
        new_subscribers = self.env['social.subscriber'].browse()
        for name in self.names.split(','):
            new_subscribers += self.env['social.subscriber'].create({
                'name': name,
                'social_service': self.social_service,
                'country_id': self.country_id.id,
            })
        # Return a list of created subscribers
        return {
            'name': _('New Subscribers'),
            'type': 'ir.actions.act_window',
            'view_mode': 'tree,form',
            'res_model': 'social.subscriber',
            'domain': [('id', 'in', new_subscribers.ids)],
        }
