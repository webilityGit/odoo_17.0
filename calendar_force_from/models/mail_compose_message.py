from odoo import api, models

class MailComposeMessage(models.TransientModel):
    _inherit = 'mail.compose.message'

    @api.model
    def create(self, vals):
        # Ako je ovaj composer pozvan za Calendar Event
        # ili imamo eksplicitni context.force_email_from,
        # forsiraj From adresu iz konteksta ili na bookings.
        if self.env.context.get('default_model') == 'calendar.event':
            vals['email_from'] = 'Winera Bookings <bookings@winera.com>'
        elif self.env.context.get('force_email_from'):
            vals['email_from'] = self.env.context['force_email_from']
        return super(MailComposeMessage, self).create(vals)
