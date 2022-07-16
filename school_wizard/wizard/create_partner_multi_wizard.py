from odoo import _, fields, models


class CreatePartnerMultiWizard(models.TransientModel):
    _name = 'create.partner.multi.wizard'
    _description = 'Wizard to create partners in easy way'

    names = fields.Char('Partner Names')
    country_id = fields.Many2one('res.country', 'Country')
    company_type = fields.Selection([('person', 'Individual'),
                                     ('company', 'Company')],
        string='Company Type',
        default='person',
    )

    def action_open_wizard(self):
        return {
            'name': _('Create Partners Wizard'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'create.partner.multi.wizard',
            'target': 'new',
            'context': {'default_country_id': self.env.user.company_id.id},
        }

    def action_create(self):
        self.ensure_one()
        for name in self.names.split(','):
            self.env['res.partner'].create({
                'name': name,
                'company_type': self.company_type,
                'country_id': self.country_id.id,
            })
