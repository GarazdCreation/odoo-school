from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class CreatePartnerMultiWizard(models.TransientModel):
    _name = 'create.partner.multi.wizard'
    _description = "Wizard to create partners in the fast way."

    names = fields.Char(
        string='Partner Names',
        required=True,
    )
    country_id = fields.Many2one(
        comodel_name='res.country',
        string='Country',
    )
    company_type = fields.Selection(
        selection=[('person', 'Individual'),
                   ('company', 'Company')],
        default='person',
    )

    def action_open_wizard(self):
        return {
            'name': _('Create Partners Wizard'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'create.partner.multi.wizard',
            'target': 'new',
            'context': {'default_country_id': self.env.user.country_id.id},
        }

    def action_create(self):
        self.ensure_one()
        for name in self.names.split(','):
            self.env['res.partner'].create({
                'name': name,
                'company_type': self.company_type,
                'country_id': self.country_id.id,
            })
