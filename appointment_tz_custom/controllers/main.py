from odoo import http
from odoo.http import request

class MyAppointmentController(http.Controller):
    @http.route(['/calendar/appointment/create', '/calendar/appointment/confirm'],
                type='http', auth='public', website=True, methods=['POST'], csrf=False)
    def calendar_appointment_create(self, appointment_id=None, **post):
        # 1) Forsiraj timezone iz zapisa termina ako hidden input nije poslao pravu vrednost
        if appointment_id:
            appt = request.env['calendar.appointment'].sudo().browse(int(appointment_id))
            if appt and appt.appointment_tz:
                post['timezone'] = appt.appointment_tz

        # 2) Pozovi originalni handler
        return super(MyAppointmentController, self).calendar_appointment_create(
            appointment_id=appointment_id, **post
        )
