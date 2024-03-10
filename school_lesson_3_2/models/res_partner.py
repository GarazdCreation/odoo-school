from dateutil.relativedelta import relativedelta

from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    gender = fields.Selection(
        selection=[
            ('male', 'Male'),
            ('female', 'Female'),
            ('other', 'Other/Undefined'),
        ],
        default='other',
    )
    join_date = fields.Date(default=fields.Date.today)
    is_verified = fields.Boolean(
        string='Verified',
        help='Partner details are filled in, and approved by a manager.',
        groups='base.group_system',
    )
    client_state = fields.Selection(
        selection=[
            ('regular', 'Regular'),
            ('loyal', 'Loyal'),
            ('vip', 'VIP'),
        ],
        string='Client Status',
        compute='_compute_client_state',
        group_operator='count',
        store=True,
    )
    client_currency_id = fields.Many2one(
        comodel_name='res.currency',
        default=lambda self: self.env.ref('base.USD').id,
        string='Bonus Currency',
    )

    @api.depends('join_date')
    def _compute_client_state(self):
        """Determine a client status of a partner. It depends on the Join Date
           If the partner join period bigger than 1 year, we set his state as "Loyal".
           If the partner join period bigger than 3 year, we set his state as "VIP".
        """
        for partner in self:
            if partner.join_date:
                join_period = relativedelta(fields.Date.today() - partner.join_date).years
                if join_period >= 3:
                    partner.client_state = 'vip'
                elif join_period >= 1:
                    partner.client_state = 'loyal'
                else:
                    partner.client_state = 'regular'
            else:
                partner.client_state = False
