# Copyright © 2024 Garazd Creation (https://garazd.biz)
# @author: Yurii Razumovskyi (support@garazd.biz)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.html).

{
    'name': 'School Lesson 3-4: Relation fields',
    'version': '17.0.1.0.0',
    'category': 'Extra Tools',
    'summary': """Odoo School Lesson 3-4: Relation fields.""",
    'license': 'LGPL-3',
    'author': 'Garazd Creation',
    'website': 'https://garazd.biz',
    'depends': [
        'school_lesson_3_3',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/social_menus.xml',
        'views/social_subscriber_views.xml',
        'views/social_promo_views.xml',
    ],
    'support': 'support@garazd.biz',
    'application': False,
    'installable': True,
    'auto_install': False,
}
