from odoo import models, api

class MailMail(models.Model):
    _inherit = 'mail.mail'

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('model') == 'calendar.attendee' and not vals.get('email_from'):
                # Proveri da li postoji šablon za calendar.attendee
                template = self.env['mail.template'].search([
                    ('model', '=', 'calendar.attendee'),
                    ('email_from', '!=', False)
                ], limit=1)
                if template:
                    vals['email_from'] = template.email_from
                else:
                    vals['email_from'] = 'Winera Bookings <bookings@winera.com>'
        return super().create(vals_list)

