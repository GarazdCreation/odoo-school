from odoo import fields, models, _


class LibraryBookCategory(models.Model):
    """ Library book categories.  """
    _inherit = 'library.book.category'

    book_ids = fields.One2many(comodel_name='library.book',
                               inverse_name='category_id',
                               string='Books')

    def action_get_books_by_category(self):
        """ Display a list of books in the current category """
        self.ensure_one()
        if self.book_ids:
            #books id for display
            related_books_ids = self.env['library.book.category'].search([
                ('book_ids.category_id', '=', self.id),
            ]).ids
            return {
                'type': 'ir.actions.act_window',
                'name': _('Books'),
                'res_model': 'library.book',
                'view_type': 'list',
                'view_mode': 'list',
                'views': [[False, 'list'], [False, 'form']],
                'domain': [('id', 'in', related_books_ids)],
            }
        return False
