# Copyright © 2022 Garazd Creation (<https://garazd.biz>)
# @author: Yurii Razumovskyi (<support@garazd.biz>)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.html).

{
    'name': 'School Lesson 6 5',
    'version': '15.0.1.0.1',
    'category': 'Extra Tools',
    'summary': """Odoo School Lesson 6-5: Module documentation. 
    """,
    'license': 'LGPL-3',
    'author': 'Garazd Creation',
    'website': 'https://garazd.biz',
    'depends': [
        'mail',
        'school_lesson_6_4',
    ],
    'data': [
        'data/ir_cron_data.xml',
        'views/library_author_views.xml',
    ],
    'support': 'support@garazd.biz',
    'application': False,
    'installable': True,
    'auto_install': False,
}
