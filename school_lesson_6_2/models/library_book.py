from odoo import fields, models, _
from odoo.exceptions import UserError


class LibraryBook(models.Model):
    _inherit = 'library.book'

    author_id = fields.Many2one(
        comodel_name='library.author',
        string='Author',
    )

    def action_take_in(self):
        self.ensure_one()
        if not self.env.user.has_group(
                'school_lesson_6_2.group_library_admin'):
            raise UserError(_("You can't take in the book. "
                              "Only library administrators can do it."))
        self.write({
            'reader_id': False,
            'taken_date': False,
        })

    def action_scrap_book(self):
        self.check_access_rule('write')
        self.write({'active': False})
