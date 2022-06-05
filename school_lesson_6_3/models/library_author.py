from odoo import fields, models, _


class LibraryAuthor(models.Model):
    _inherit = 'library.author'

    biography = fields.Text(translate=True)

    def action_book_list(self):
        self.ensure_one()
        return {
            'name': _('Author Books'),
            'type': 'ir.actions.act_window',
            'view_mode': 'tree,form',
            'res_model': 'library.book',
            'context': {'default_author_id': self.id},
            'domain': [('author_id', '=', self.id)],
        }
