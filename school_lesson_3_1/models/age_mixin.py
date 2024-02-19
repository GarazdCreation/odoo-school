from datetime import date
from dateutil.relativedelta import relativedelta

from odoo import api, fields, models


class AgeMixin(models.AbstractModel):
    _name = "age.mixin"
    _description = 'Mixin to calculate an age'

    birthday = fields.Date(string='Date of Birth')
    age = fields.Integer(compute='_compute_age')

    @api.depends('birthday')
    def _compute_age(self):
        for rec in self:
            if rec.birthday:
                rec.age = relativedelta(
                    date.today(),
                    date(rec.birthday.year, rec.birthday.month, rec.birthday.day),
                ).years
            else:
                rec.age = False
