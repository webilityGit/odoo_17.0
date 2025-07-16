from odoo import models
import logging

_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        # Add context flag to suppress confirmation email
        self = self.with_context(skip_sale_email=True)
        return super(SaleOrder, self).action_confirm()

    def _send_order_confirmation_mail(self):
        """ Send a mail to the SO customer to inform them that their order has been confirmed. """
        if self.env.context.get('skip_sale_email'):
            _logger.info('Skipping order confirmation email for SO: %s', self.ids)
            return
        return super(SaleOrder, self)._send_order_confirmation_mail()