from odoo.addons.school_lesson_6_4.tests.common import TestCommon
from odoo.tests import tagged
from odoo.exceptions import AccessError


@tagged('post_install', '-at_install', 'library', 'access')
class TestAccessRights(TestCommon):

    def test_library_user_access_rights(self):
        with self.assertRaises(AccessError):
            self.env['library.book'].with_user(self.library_user).create(
                {'name': 'Test Book'})
        with self.assertRaises(AccessError):
            self.book_demo.with_user(self.library_user).unlink()
