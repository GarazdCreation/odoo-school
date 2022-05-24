from odoo.tests.common import TransactionCase


class TestCommon(TransactionCase):

    def setUp(self):
        super(TestCommon, self).setUp()
        self.group_library_user = self.env.ref(
            'school_lesson_6_2.group_library_user')
        self.group_library_admin = self.env.ref(
            'school_lesson_6_2.group_library_admin')
        self.library_user = self.env['res.users'].create({
            'name': 'Library User',
            'login': 'library_user',
            'groups_id': [(4, self.env.ref('base.group_user').id),
                          (4, self.group_library_user.id)],
        })
        self.library_admin = self.env['res.users'].create({
            'name': 'Library Admin',
            'login': 'library_admin',
            'groups_id': [(4, self.env.ref('base.group_user').id),
                          (4, self.group_library_admin.id)],
        })
        self.reader = self.env['res.partner'].create({'name': 'Demo Reader'})
        self.book_demo = self.env['library.book'].create({
            'name': 'Demo Book'})
