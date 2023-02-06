from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    telegram = fields.Char(
        string='Telegram Nickname',
    )
