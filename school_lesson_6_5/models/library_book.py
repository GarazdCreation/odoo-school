from odoo import api, fields, models


class LibraryBook(models.Model):
    _inherit = 'library.book'

    def set_type_book(self):
        """Set the type "Book" for records."""
        self.write({'type': 'book'})
