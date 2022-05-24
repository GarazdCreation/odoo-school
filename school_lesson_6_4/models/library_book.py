from odoo import api, fields, models


class LibraryBook(models.Model):
    _inherit = 'library.book'

    @api.model
    def default_get(self, fields_list):
        default_vals = super(LibraryBook, self).default_get(fields_list)
        if 'type' in fields_list and not default_vals.get('type'):
            default_vals['type'] = 'book'
        return default_vals

    type = fields.Selection(
        selection=[
            ('brochure', 'Brochure'),
            ('book', 'Book'),
            ('encyclopedia', 'Encyclopedia'),
        ],
        string='Type',
    )
