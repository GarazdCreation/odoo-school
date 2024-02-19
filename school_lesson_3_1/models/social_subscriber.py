from odoo import fields, models


class SocialSubscriber(models.Model):
    _name = 'social.subscriber'
    _inherits = {'res.partner': 'partner_id'}

    partner_id = fields.Many2one(
        comodel_name='res.partner',
        ondelete='cascade',
        index=True,
    )
    social_service = fields.Selection(
        selection=[
            ('instagram', 'Instagram'),
            ('tiktok', 'TikTok'),
            ('youtube', 'YouTube'),
        ],
        required=True,
    )

