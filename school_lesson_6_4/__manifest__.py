# Copyright © 2022 Garazd Creation (<https://garazd.biz>)
# @author: Yurii Razumovskyi (<support@garazd.biz>)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.html).

{
    'name': 'School Lesson 6 4',
    'version': '15.0.0.0.1',
    'category': 'Extra Tools',
    'summary': """
        Odoo School
        Lesson 6-4: Writing tests. 
    """,
    'license': 'LGPL-3',
    'author': 'Garazd Creation',
    'website': 'https://garazd.biz',
    'depends': [
        'school_lesson_6_3',
    ],
    'data': [
        'views/library_templates.xml',
        'views/library_book_views.xml',
    ],
    'support': 'support@garazd.biz',
    'application': False,
    'installable': True,
    'auto_install': False,
}
