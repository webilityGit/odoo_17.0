from odoo import models, api

class MailMail(models.Model):
    _inherit = 'mail.mail'

    @api.model
    def create(self, vals):
        if vals.get('model') == 'calendar.attendee' and not vals.get('email_from'):
            # Pronađi šablon za calendar.attendee ako postoji i koristi njegov email_from
            template = self.env['mail.template'].search([('model', '=', 'calendar.attendee'), ('email_from', '!=', False)], limit=1)
            if template:
                vals['email_from'] = template.email_from
            else:
                # Fallback adresa ako nema šablona
                vals['email_from'] = 'Winera Bookings <bookings@winera.com>'
        return super().create(vals)
