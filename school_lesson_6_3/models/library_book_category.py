from odoo import models, fields, api


class LibraryBookCategory(models.Model):
    """The LibraryBookCategory class represents a book category in the library.

    This class extends the standard model from the module school_lesson_6_1 in
    and is used for managing book
    categories in a library. It allows for the categorization of books into
    various categories, facilitating their search and management."""

    _inherit = 'library.book.category'

    book_ids = fields.One2many(
        comodel_name='library.book',
        inverse_name='category_id',
        string="Books")

    @api.depends('book_ids')
    def get_books_list(self):
        """Returns a list of all books that belong to current category."""
        book_names = self.book_ids.mapped('name')
        books_list_str = ', '.join(book_names)
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Books in this Category',
                'message': books_list_str,
                'sticky': True,
            },
        }
