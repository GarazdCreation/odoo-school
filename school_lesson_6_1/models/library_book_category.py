from odoo import models, fields


class LibraryBookCategory(models.Model):
    _name = 'library.book.category'
    _description = 'Library Book Category'

    name = fields.Char(
        string='Category Name', required=True)
    active = fields.Boolean(
        default=True, )
