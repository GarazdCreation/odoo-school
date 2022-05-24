import odoo.http as http

from odoo.http import request


class LibraryController(http.Controller):

    @http.route('/library/books', type='http', auth='user')
    def accept_meeting(self):
        user = request.env['res.users'].sudo().browse(request.session.uid)
        books = request.env['library.book'].search([
            ('reader_id', '=', user.partner_id.id)])
        response_content = request.env['ir.ui.view'].with_context(
            lang=user.lang)._render_template(
                'school_lesson_6_4.library_books_page', {
                    'company': user.company_id,
                    'reader': user.partner_id,
                    'books': books,
                })
        return request.make_response(
            response_content, headers=[('Content-Type', 'text/html')])
