from datetime import date

from odoo import api, fields, models, _


class LibraryAuthor(models.Model):
    _name = 'library.author'
    _inherit = ['library.author', 'mail.thread', 'mail.activity.mixin']

    @api.model
    def calculate_author_anniversary(self, notify_type='todo'):
        """Determine author anniversaries for the current month.
        If the anniversary is in the current month an activity will be created.

        :param notify_type: can have two value "todo" or "meeting",
                            determine which activity type to create.
        :return None:
        """
        activity_types = {
            'todo': 'mail.mail_activity_data_todo',
            'meeting': 'mail_activity_data_meeting',
        }
        if notify_type not in activity_types.keys():
            return None
        authors = self.env['library.author'].search([
            ('birth_date', '!=', False)])
        for author in authors:
            # Get only those authors whose century anniversary
            # is in the current month
            if (fields.Date.today().year - author.birth_date.year) % 100 and \
                    fields.Date.today().month == author.birth_date.month:
                self.env['mail.activity'].create({
                    'res_model_id': self.env.ref(
                        'school_lesson_6_2.model_library_author').id,
                    'res_id': author.id,
                    'activity_type_id': self.env.ref(
                        activity_types[notify_type]).id,
                    'user_id': self.env.ref('base.user_admin').id,
                    'summary': _("%s anniversary is coming soon.",
                                 author.display_name),
                    'date_deadline': fields.Date.to_string(date(
                        fields.Date.today().year,
                        author.birth_date.month,
                        author.birth_date.day))
                })

    def get_bk_cnt(self):
        """This sample method shows a BAD approach for naming."""
        self.ensure_one()
        bc = self.env['library.book'].search_count([
            ('author_id', '=', self.id)])
        return bc

    def get_book_count(self):
        """This sample method shows GOOD approach for naming."""
        self.ensure_one()
        book_count = self.env['library.book'].search_count([
            ('author_id', '=', self.id)])
        return book_count
