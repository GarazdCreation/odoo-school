from odoo import fields, models


class ResLang(models.Model):
    _inherit = 'res.lang'

    color = fields.Integer(string='Color Index', default=0)
