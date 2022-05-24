from odoo.tests import HttpCase, tagged


@tagged('post_install', '-at_install', 'library')
class TestAccessRights(HttpCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user_password = "info"
        cls.user = cls.env['res.users'].create({
            'name': 'Library User Http',
            'login': 'library_user_http',
            'password': cls.user_password,
            'groups_id': [
                (4, cls.env.ref('base.group_user').id),
                (4, cls.env.ref('school_lesson_6_2.group_library_user').id)
            ],
        })

    def test_http(self):
        self.authenticate(self.user.login, self.user_password)
        r = self.url_open('/library/books')
        self.assertTrue(r.ok, r.text)
        self.assertTrue(
            "Books in use of" in r.text,
            "Table title must be in the page.")
