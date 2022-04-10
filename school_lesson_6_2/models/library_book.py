from odoo import fields, models


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Books'

    name = fields.Char('Title')
    reader_id = fields.Many2one(
        comodel_name='res.partner',
        string='Reader',
    )

    def action_assign_default(self):
        self.ensure_one()
        self.reader_id = self.env.ref(
            'school_lesson_6_1.res_partner_customer').id

