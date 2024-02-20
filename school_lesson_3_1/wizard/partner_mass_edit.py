from odoo import fields, models


class PartnerMassEdit(models.TransientModel):
    _name = "partner.mass.edit"
    _description = 'Wizard for mass editing of partners'
    _transient_max_count = 1000
    _transient_max_hours = 3

    partner_ids = fields.Many2many(
        comodel_name='res.partner',
        string='Partners',
    )
    channel = fields.Selection(
        selection=[
            ('email', 'Email'),
            ('telegram', 'Telegram'),
            ('whatsapp', 'WhatsApp'),
        ],
        string='Communication Channel',
        help='Main communication channel with the partner.',
        required=True,
    )

    def action_mass_edit(self):
        self.ensure_one()
        self.partner_ids.write({'channel': self.channel})
        return {'type': 'ir.actions.act_window_close'}
