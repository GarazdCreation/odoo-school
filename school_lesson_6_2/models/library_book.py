from odoo import fields, models


class LibraryBook(models.Model):
    _inherit = 'library.book'

    author_id = fields.Many2one(
        comodel_name='library.author',
        string='Author',
    )
