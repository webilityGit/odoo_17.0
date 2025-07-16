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