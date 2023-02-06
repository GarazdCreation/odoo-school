# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.html).

{
    'name': 'My Library',
    'version': '15.0.1.0.0',
    'category': 'Extra Tools',
    'summary': """My Library (sample for Module 2).""",
    'license': 'LGPL-3',
    'author': 'Odoo School',
    'website': 'https://odoo.school',
    'depends': [
        'base',
        'contacts',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/library_menus.xml',
        'views/library_book_views.xml',
        'views/library_rental_views.xml',
        'views/res_partner_views.xml',
    ],
    'demo': [
        'data/library_genre_demo.xml',
    ],
    'support': 'support@garazd.biz',
    'application': False,
    'installable': True,
    'auto_install': False,
}
