from odoo import fields, models


class LibraryBook(models.Model):
    _inherit = 'library.book'

    description = fields.Text(translate=True)
