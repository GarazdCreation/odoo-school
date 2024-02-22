from odoo import fields, models


class SocialPromo(models.Model):
    _name = 'social.promo'
    _description = 'Social Promotions'

    name = fields.Char(required=True)
    subscriber_id = fields.Many2one(
        comodel_name='social.subscriber',
        ondelete='cascade',
        required=True,
    )
