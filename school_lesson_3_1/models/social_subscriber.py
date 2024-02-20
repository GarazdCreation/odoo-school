from odoo import fields, models


class SocialSubscriber(models.Model):
    _name = 'social.subscriber'
    _inherits = {'res.partner': 'partner_id'}
    _description = 'Subscribers from Social Networks'

    partner_id = fields.Many2one(
        comodel_name='res.partner',
        ondelete='cascade',
        required=True,
        index=True,
    )
    social_service = fields.Selection(
        selection=[
            ('undefined', 'Undefined'),
            ('instagram', 'Instagram'),
            ('tiktok', 'TikTok'),
            ('youtube', 'YouTube'),
        ],
        default='undefined',
        required=True,
    )

