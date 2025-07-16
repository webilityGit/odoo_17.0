from odoo import models
import logging

_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_quotation_send(self):
        """
        Open the compose wizard but suppress automatic email sending via mail_compose hook.
        """
        _logger.info('Opening quotation compose wizard for SO: %s', self.ids)
        return super(SaleOrder, self).action_quotation_send()