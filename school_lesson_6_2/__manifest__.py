# Copyright © 2022 Garazd Creation (<https://garazd.biz>)
# @author: Yurii Razumovskyi (<support@garazd.biz>)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.html).

{
    'name': 'School Lesson 6 2',
    'version': '15.0.0.0.1',
    'category': 'Extra Tools',
    'summary': """
        Odoo School
        Lesson 6-2: Access rights and record rules. 
    """,
    'license': 'LGPL-3',
    'author': 'Garazd Creation',
    'website': 'https://garazd.biz',
    'depends': [
        'school_lesson_6_1',
    ],
    'data': [
        'security/library_book_groups.xml',
        'security/ir.model.access.csv',
        'security/library_book_security.xml',
        'views/library_author_views.xml',
        'views/library_book_views.xml',
    ],
    'support': 'support@garazd.biz',
    'application': False,
    'installable': True,
    'auto_install': False,
}
