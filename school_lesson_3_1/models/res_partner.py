from odoo import fields, models


class ResPartner(models.Model):
    _name = 'res.partner'
    _inherit = ['age.mixin', 'res.partner']

    channel = fields.Selection(
        selection=[
            ('email', 'Email'),
            ('telegram', 'Telegram'),
            ('whatsapp', 'WhatsApp'),
        ],
        string='Communication Channel',
        help='Main communication channel with the partner.',
    )
