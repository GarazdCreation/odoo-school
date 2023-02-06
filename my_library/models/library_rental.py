from odoo import fields, models


class LibraryRental(models.Model):
    _name = 'library.rental'
    _description = 'Library Book Rentals'
    _rec_name = 'book_id'
    _order = 'start_date DESC, end_date DESC'

    book_id = fields.Many2one(
        comodel_name='library.book',
        ondelete='cascade',
        required=True,
    )
    reader_id = fields.Many2one(
        comodel_name='res.partner',
        string='Reader',
        required=True,
    )
    start_date = fields.Datetime(
        string='Rent Started',
        default=fields.Datetime.now(),
        required=True,
    )
    end_date = fields.Datetime(
        string='Book Returned',
        readonly=True,
    )
    book_state = fields.Selection(related='book_id.state')

    def action_give_book(self):
        self.ensure_one()
        self.book_id.write({
            'state': 'in_use',
        })

    def action_return_book(self):
        self.ensure_one()
        self.end_date = fields.Datetime.now()
        self.book_id.write({'state': 'ready'})
