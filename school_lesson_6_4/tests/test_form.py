from odoo import fields
from odoo.tests import tagged
from odoo.tests.common import Form
from odoo.addons.school_lesson_6_4.tests.common import TestCommon


@tagged('post_install', '-at_install', 'library')
class TestForm(TestCommon):

    def test_book_taken_date(self):
        book_form = Form(self.book_demo)

        book_form.reader_id = self.library_user.partner_id
        self.assertEqual(book_form.taken_date, fields.Date.today())

        book_form.reader_id = self.library_user.partner_id
        self.assertEqual(book_form.taken_date, fields.Date.today())
