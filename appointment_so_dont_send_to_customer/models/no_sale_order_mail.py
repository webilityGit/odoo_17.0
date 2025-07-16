from odoo import models, api
import logging

_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.multi
    def action_quotation_send(self):
        """
        Override to open the compose wizard but suppress the actual send via mail_compose.
        """
        _logger.info('Opening quotation compose wizard for SO: %s', self.ids)
        return super(SaleOrder, self).action_quotation_send()


from odoo import models
import logging

_logger = logging.getLogger(__name__)

class MailComposeMessage(models.TransientModel):
    _inherit = 'mail.compose.message'

    def send_mail(self, auto_commit=False):
        # Suppress sending emails when composing for sale.order
        if self.model == 'sale.order':
            _logger.info('Suppressed sending quotation email for SO compose: %s', self.res_id)
            return True
        return super(MailComposeMessage, self).send_mail(auto_commit=auto_commit)