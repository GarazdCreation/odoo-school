from odoo import _, fields, models


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Books'

    name = fields.Char(string='Title', required=True)
    genre_id = fields.Many2one(
        comodel_name='library.genre',
        string='Genre',
        ondelete='set null',
    )
    author_ids = fields.Many2many(
        comodel_name='res.partner',
        string='Authors',
    )
    publish_date = fields.Date(
        string='Published on',
        default=fields.Date.today,
        help='The date when the book was published.',
    )
    state = fields.Selection(
        selection=[
            ('ready', 'Ready to rent'),
            ('in_use', 'In use'),
        ],
        string='Status',
        default='ready',
    )

    def action_log_rent(self):
        self.ensure_one()
        return {
            'name': _('Give to reader'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'library.rental',
            'context': {'default_book_id': self.id},
            'target': 'new',
        }

    def action_open_author_list(self):
        self.ensure_one()
        return {
            'name': _('Authors'),
            'type': 'ir.actions.act_window',
            'view_mode': 'tree,form',
            'res_model': 'res.partner',
            'domain': [('id', 'in', self.author_ids.ids)],
            'target': 'current',
        }
