from odoo import http
from odoo.http import request

class WebsiteCalendarLockTz(http.Controller):
    @http.route(
        ['/calendar/appointment/<int:appointment_id>'],
        type='http', auth='public', website=True
    )
    def appointment(self, appointment_id, **post):
        # Učitaj termin i prosledi u template
        appointment = request.env['calendar.appointment'].sudo().browse(appointment_id)
        return request.render(
            'website_timezone_lock.appointment_form_force_tz',
            {
                'appointment_id': appointment,
                # ostali potrebni kontekst parametri iz originala
            }
        )