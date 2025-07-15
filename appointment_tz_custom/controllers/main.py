from odoo import http
from odoo.http import request

class WebsiteAppointmentLock(http.Controller):

    @http.route([
        '/calendar/appointment/create',
        '/calendar/appointment/confirm',
    ], type='http', auth='public', website=True, methods=['POST'], csrf=False)
    def calendar_appointment_create(self, appointment_id=None, **post):
        # učitajte appointment record
        if appointment_id:
            appointment = request.env['calendar.appointment'].sudo().browse(int(appointment_id))
            # forsirajte post['timezone']
            post['timezone'] = appointment.appointment_tz

        # zatim pozovite originalni kod (kopirajte iz website_appointment/controllers/main.py)
        return super(WebsiteAppointmentLock, self).calendar_appointment_create(**post)
