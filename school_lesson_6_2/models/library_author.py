from datetime import datetime, timedelta

from odoo import fields, models


class LibraryAuthor(models.Model):
    _name = 'library.author'
    _description = 'Library Book Authors'

    first_name = fields.Char(required=True)
    last_name = fields.Char(required=True)
    birth_date = fields.Date('Birthday')
    is_under_30_day = fields.Boolean(compute='_is_under_30_day')

    def name_get(self):
        return [(rec.id, "%s %s" % (rec.first_name, rec.last_name))
                for rec in self]

    def action_delete(self):
        self.ensure_one()
        self.check_access_rights('unlink')
        self.unlink()

    def _create_by_user(self, vals):
        return self.sudo().create(vals)

    def _is_under_30_day(self):
        for rec in self:
            rec.is_under_30_day = rec.create_date > datetime.now() - timedelta(
                days=30)
