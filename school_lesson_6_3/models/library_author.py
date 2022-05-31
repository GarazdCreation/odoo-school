from odoo import fields, models


class LibraryAuthor(models.Model):
    _inherit = 'library.author'

    biography = fields.Text(translate=True)
