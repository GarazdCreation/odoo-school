from odoo import api, fields, models


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Books'

    name = fields.Char('Title')
    reader_id = fields.Many2one(
        comodel_name='res.partner',
        string='Reader',
    )
    taken_date = fields.Date('In use from', readonly=True)
    user_id = fields.Many2one(
        comodel_name='res.users',
        string='Responsible',
    )
    active = fields.Boolean(
        string='Active',
        default=True,
    )

    @api.onchange('reader_id')
    def _onchange_reader_id(self):
        if self.reader_id and not self.taken_date:
            self.taken_date = fields.Date.today()

    def action_assign_default(self):
        self.ensure_one()
        self.reader_id = self.env.ref(
            'school_lesson_6_1.res_partner_customer').id

