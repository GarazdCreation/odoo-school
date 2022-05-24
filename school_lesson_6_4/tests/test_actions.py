from odoo.addons.school_lesson_6_4.tests.common import TestCommon
from odoo.tests import tagged
from odoo.exceptions import UserError


@tagged('post_install', '-at_install', 'library')
class TestAccessRights(TestCommon):

    def test_action_take_in(self):
        self.book_demo.write({'reader_id': self.library_user.partner_id.id})

        # A library user can't return a book himself
        with self.assertRaises(UserError):
            self.book_demo.with_user(self.library_user).action_take_in()

        # A library admin can return a book
        self.book_demo.with_user(self.library_admin).action_take_in()
        self.assertFalse(self.book_demo.reader_id)

