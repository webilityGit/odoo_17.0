from odoo import models, api, _
import logging

_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_quotation_send(self):
        """
        Override to suppress sending quotation email to customer for website bookings.
        """
        # Log suppression
        _logger.info('SO quotation email suppressed for orders: %s', self.ids)
        # Do not call super: skip email sending
        return True

