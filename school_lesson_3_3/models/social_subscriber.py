from odoo import fields, models


class SocialSubscriber(models.Model):
    _inherit = 'social.subscriber'
    _order = 'sequence'

    sequence = fields.Integer(default=100)
    nickname = fields.Char(size=8, trim=False, translate=False)
    state = fields.Selection(
        selection=[
            ('new', 'New'),
            ('registered', 'Registered'),
        ],
        string='Status',
        default='new',
    )
    is_confirmed = fields.Boolean(string='Contact is Confirmed', readonly=True)
    client_bonus = fields.Monetary(
        string='Bonus Amount',
        currency_field='client_currency_id',
        readonly=True,
        copy=False,
    )
    notes = fields.Text(string='Description', translate=True)
    profile = fields.Html(sanitize=True)
    passport = fields.Binary(attachment=True)
    photo = fields.Image(
        max_width=100,
        max_height=100,
        verify_resolution=True,
    )
    social_service = fields.Selection(
        selection_add=[
            ('facebook', 'Facebook'),
        ],
        ondelete={
            # 'facebook': 'cascade',
            # 'facebook': 'set default',
            # 'facebook': 'set null',
            # 'facebook': 'set undefined',
            'facebook': lambda recs: recs.write({'social_service': 'undefined'}),
        },
        # The actions can be any of the following:
        #   - 'set null' -- the default, all records with this option will have their selection value set to False.
        #   - 'cascade' -- all records with this option will be deleted along with the option itself.
        #   - 'set default' -- all records with this option will be set to the default of the field definition
        #   - 'set VALUE' -- all records with this option will be set to the given value
        #   - <callable> -- a callable whose first and only argument will be the set of records containing the
        #     specified Selection option, for custom processing
    )
    start_date = fields.Date(string='Started')
    end_date = fields.Date(string='Finished')




