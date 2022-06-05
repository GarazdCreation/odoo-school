from odoo import fields, models, _lt
from odoo.exceptions import UserError

ERR_MSG = _lt("You can't lend a book in advance.")


class LibraryBook(models.Model):
    _inherit = 'library.book'

    description = fields.Text(translate=True)

    def write(self, vals):
        if vals.get('taken_date') and \
                vals.get('taken_date') > fields.Date.today():
            raise UserError(ERR_MSG)
        return super(LibraryBook, self).write(vals)
