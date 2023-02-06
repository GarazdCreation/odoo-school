# Copyright © 2022 Garazd Creation (<https://garazd.biz>)
# @author: Yurii Razumovskyi (<support@garazd.biz>)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.html).

{
    'name': 'School Lesson 6 1',
    'version': '15.0.0.0.1',
    'category': 'Extra Tools',
    'summary': """
        Odoo School
        Lesson 6-1: Master and demo data.
Task 1.4
    """,
    'license': 'LGPL-3',
    'author': 'Garazd Creation',
    'website': 'https://garazd.biz',
    'depends': [
        'base',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/res_partner_data.xml',
        'views/library_book_menus.xml',
        'views/library_book_views.xml',
    ],
    'demo': [
        'data/res_partner_demo.xml',
        'data/res_partner_bank_demo.xml',
    ],
    'support': 'support@garazd.biz',
    'application': False,
    'installable': True,
    'auto_install': False,
}
