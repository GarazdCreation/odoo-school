import logging

from odoo import _, fields, models
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)


class SocialSubscriber(models.Model):
    _inherit = 'social.subscriber'

    client_bonus = fields.Monetary(group_operator='sum')

    def action_get_promo(self):
        self.ensure_one()
        return {
            'name': _('Social Promotions'),
            'type': 'ir.actions.act_window',
            'res_model': 'social.promo',
            'view_mode': 'tree',
            'context': {'default_subscriber_id': self.id},
            'domain': [('id', 'in', self.promo_ids.ids)],
        }

    def action_show_subscribers_of_same_social(self):
        self.ensure_one()
        same_social_subscribers = self.search([('social_service', '=', self.social_service)])
        return {
            'name': _('Social "%s" Subscribers', self.social_service),
            'type': 'ir.actions.act_window',
            'res_model': self._name,
            'view_mode': 'tree,form',
            'domain': [('id', 'in', same_social_subscribers.ids)],
        }

    def get_sorted_list_by_bonus(self):
        subscribers = self.search([])
        sorted_by_bonus_list = subscribers.sorted(
            key=lambda s: s.client_bonus, reverse=True,
        ).mapped('client_bonus')
        # _logger.info("--- Subscriber Sorted List ---\n%s", '\n'.join(sorted_by_bonus_list))
        raise UserError(_(
            "Subscriber Sorted List: %s",
            sorted_by_bonus_list,
        ))

    def action_extra_processing(self):
        # flake8: noqa: E501
        domain = [('id', 'in', self._context.get('active_ids', []))]

        # The "search_read" method - is used for optimization of the search and read requests
        # -----------------------------------------------------------------------------------
        subscribers = self.search_read(fields=['id', 'social_service', 'is_confirmed'])
        # RESULT: subscribers = [
        #     {'id': 1, 'social_service': 'instagram', 'is_confirmed': True},
        #     {'id': 2, 'social_service': 'facebook', 'is_confirmed': False},
        #     {'id': 3, 'social_service': 'tiktok', 'is_confirmed': False},
        #     {'id': 4, 'social_service': 'facebook', 'is_confirmed': True},
        #     {'id': 5, 'social_service': 'youtube', 'is_confirmed': False}
        # ]
        for subscriber in subscribers:
            # RESULT: subscriber (the 1st iteration) = {'id': 1, 'is_confirmed': True, 'social_service': 'instagram'}
            pass

        # The "read_group" method - is used for get grouped records
        # ---------------------------------------------------------
        subscriber_groups = self.read_group(domain, ['social_service', 'id:array_agg'], ['social_service'])
        for group in subscriber_groups:
            # RESULTS:
            # group (the 1st iteration) = {
            #     '__domain': ['&', ('id', 'in', [1, 2, 3, 4, 5]), ('social_service', '=', 'facebook')],
            #     'id': [2, 4],
            #     'social_service': 'facebook',
            #     'social_service_count': 2
            # }
            # group (the 2nd iteration) = {
            #     '__domain': ['&', ('id', 'in', [1, 2, 3, 4, 5]), ('social_service', '=', 'instagram')],
            #     'id': [1],
            #     'social_service': 'instagram',
            #     'social_service_count': 1
            # }
            # group (the 3rd iteration) = {
            #     '__domain': ['&', ('id', 'in', [1, 2, 3, 4, 5]), ('social_service', '=', 'tiktok')],
            #     'id': [3],
            #     'social_service': 'tiktok',
            #     'social_service_count': 1
            # }
            # group (the 4th iteration) = {
            #     '__domain': ['&', ('id', 'in', [1, 2, 3, 4, 5]), ('social_service', '=', 'youtube')],
            #     'id': [5],
            #     'social_service': 'youtube',
            #     'social_service_count': 1
            # }
            pass

        # The "read_group" method - with group by date periods
        subscriber_groups = self.read_group(
            domain=domain,
            fields=['social_service', 'id:array_agg'],
            groupby=['start_date:month'],
        )
        for group in subscriber_groups:
            # RESULTS:
            # group (the 1st iteration) = {
            #     'start_date:month': 'January 2024',
            #     'start_date_count': 1,
            #     'id': [5],
            #     '__domain': [
            #         '&', ('id', 'in', [1, 2, 3, 4, 5]), '&', ('start_date', '>=', '2024-01-01'), ('start_date', '<', '2024-02-01')
            #     ],
            #     '__range': {'start_date:month': {'from': '2024-01-01', 'to': '2024-02-01'}}
            # }
            # group (the 2nd iteration) = {
            #     'start_date:month': 'February 2024',
            #     'start_date_count': 4,
            #     'id': [1, 2, 3, 4],
            #     '__domain': [
            #         '&', ('id', 'in', [1, 2, 3, 4, 5]), '&', ('start_date', '>=', '2024-02-01'), ('start_date', '<', '2024-03-01')
            #     ],
            #     '__range': {'start_date:month': {'from': '2024-02-01', 'to': '2024-03-01'}}
            # }
            pass

            # The "read_group" method - with aggregation by sum
            subscriber_groups = self.read_group(
                domain=domain,
                fields=['social_service', 'id:array_agg', 'client_bonus'],
                groupby=['social_service'],
            )
            # RESULT: subscriber_groups = [
            # {
            #     'social_service': 'facebook',
            #     'social_service_count': 2,
            #     'id': [2, 4],
            #     'client_bonus': 85.05,
            #     '__domain': ['&', ('id', 'in', [1, 2, 3, 4, 5]), ('social_service', '=', 'facebook')]
            # },
            # {
            #     'social_service': 'instagram', 'social_service_count': 1, 'id': [1], 'client_bonus': 25.0,
            #     '__domain': ['&', ('id', 'in', [1, 2, 3, 4, 5]), ('social_service', '=', 'instagram')]
            # },
            # {
            #     'social_service': 'tiktok',
            #     'social_service_count': 1,
            #     'id': [3],
            #     'client_bonus': 120.2,
            #     '__domain': ['&', ('id', 'in', [1, 2, 3, 4, 5]), ('social_service', '=', 'tiktok')]
            # },
            # {
            #     'social_service': 'youtube',
            #     'social_service_count': 1,
            #     'id': [5],
            #     'client_bonus': 5.1,
            #     '__domain': ['&', ('id', 'in', [1, 2, 3, 4, 5]), ('social_service', '=', 'youtube')]
            # }]

            # The "exist" method - is used to ensure that all records exist at the moment the method call
            # -------------------------------------------------------------------------------------------
            subscribers = self.env['social.subscriber'].browse(self._context.get('active_ids', [])).exists()
            # RESULT: subscribers = social.subscriber(1, 2, 3, 4, 5)

            # The "grouped" method - is used for get grouped records
            # ------------------------------------------------------
            social_services = subscribers.grouped('social_service')
            # RESULT: social_services = {
            #     'facebook': social.subscriber(2, 4),
            #     'instagram': social.subscriber(1, ),
            #     'tiktok': social.subscriber(3, ),
            #     'youtube': social.subscriber(5, )
            # }

            # The "get_metadata" method - to get metadata of a record
            # -------------------------------------------------------
            meta_data = self.env.ref('school_lesson_3_4.subscriber_tom').get_metadata()
            # RESULT: meta_data = [{
            #     'id': 1,
            #     'create_uid': (1, 'OdooBot'),
            #     'create_date': datetime.datetime(2024, 2, 22, 6, 16, 43, 146737),
            #     'write_uid': (1, 'OdooBot'),
            #     'write_date': datetime.datetime(2024, 2, 22, 11, 26, 31, 742115),
            #     'xmlid': 'school_lesson_3_4.subscriber_tom',
            #     'noupdate': True,
            #     'xmlids': [{'xmlid': 'school_lesson_3_4.subscriber_tom', 'noupdate': True}]
            # }]

            # The "filtered_domain" method - to filter records by a domain
            # ------------------------------------------------------------
            filtered_subscribers = subscribers.filtered_domain([('social_service', '=', 'facebook')])
            # RESULT: filtered_subscribers = social.subscriber(2, 4)

        return {'type': 'ir.actions.act_window_close'}
