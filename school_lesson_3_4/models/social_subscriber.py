from odoo import api, fields, models


class SocialSubscriber(models.Model):
    _inherit = 'social.subscriber'

    @api.model
    def _selection_target_model(self):
        return [(model.model, model.name) for model in self.env['ir.model'].sudo().search([])]

    # Many2one
    bank_id = fields.Many2one(
        comodel_name='res.bank',
        string='Local Bank',
        ondelete='restrict',
        help='The main bank of the subscriber.',
    )
    # Many2many
    language_ids = fields.Many2many(
        comodel_name='res.lang',
        relation='social_subscriber_res_lang_rel',
        column1='subscriber_id',
        column2='language_id',
        string='Known Languages',
    )
    # One2many
    promo_ids = fields.One2many(
        comodel_name='social.promo',
        inverse_name='subscriber_id',
        string='Promotions',
    )
    # Reference
    any_record_ref = fields.Reference(
        string='Any Record',
        selection='_selection_target_model',
    )
    # Many2oneReference
    res_model_id = fields.Many2one('ir.model', 'Model', index=True, ondelete='cascade')
    res_model = fields.Char(string='Model Name', related='res_model_id.model', store=True, index=True, readonly=True)
    res_id = fields.Many2oneReference(string='Resource ID', model_field='res_model', index=True)
    resource_ref = fields.Reference(
        selection='_selection_target_model',
        compute='_compute_resource_ref',
        readonly=True,
        store=True,
    )

    @api.depends('res_model', 'res_id')
    def _compute_resource_ref(self):
        for rec in self:
            if rec.res_model and rec.res_model in self.env:
                rec.resource_ref = '%s,%s' % (rec.res_model, rec.res_id or 0)
            else:
                rec.resource_ref = None

    def action_remove_promo(self):
        self.ensure_one()
        self.promo_ids = [(5, 0, 0)]
