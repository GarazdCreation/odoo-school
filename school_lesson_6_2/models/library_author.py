from odoo import fields, models


class LibraryAuthor(models.Model):
    _name = 'library.author'
    _description = 'Library Book Authors'

    first_name = fields.Char(required=True)
    last_name = fields.Char(required=True)
    birth_date = fields.Date('Birthday')

