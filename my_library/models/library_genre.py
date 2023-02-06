from odoo import fields, models


class LibraryGenre(models.Model):
    _name = 'library.genre'
    _description = 'Library Book Genres'

    name = fields.Char(required=True)
