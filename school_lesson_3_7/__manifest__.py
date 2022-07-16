# Copyright © 2022 Garazd Creation (<https://garazd.biz>)
# @author: Yurii Razumovskyi (<support@garazd.biz>)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.html).

{
    'name': 'School Lesson 3 7',
    'version': '15.0.0.0.1',
    'category': 'Extra Tools',
    'summary': """
        Odoo School
        Lesson 3-7: Wizards. Temporary models. 
    """,
    'license': 'LGPL-3',
    'author': 'Garazd Creation',
    'website': 'https://garazd.biz',
    'depends': ['contacts'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/create_partner_multi_wizard_views.xml',
    ],
    'support': 'support@garazd.biz',
    'application': False,
    'installable': True,
    'auto_install': False,
}
