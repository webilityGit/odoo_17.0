from odoo import http
from odoo.http import request
from odoo.addons.website_calendar.controllers.main import WebsiteCalendar

class WebsiteCalendarTZLock(WebsiteCalendar):
    # Override prikaza forme
    @http.route(['/calendar/appointment/<int:appointment_id>'],
                type='http', auth='public', website=True)
    def appointment(self, appointment_id, **post):
        appt = request.env['calendar.appointment'].sudo().browse(appointment_id)
        # ubaci appointment_tz u JS options
        values = {
            'appointment_id': appt,
            'options': {
                'appointment_tz': appt.appointment_tz,
            },
        }
        return request.render('appointment_tz_lock.appointment_form', values)

    # Override prijema podataka iz forme
    @http.route(['/calendar/appointment/create', '/calendar/appointment/confirm'],
                type='http', auth='public', website=True,
                methods=['POST'], csrf=False)
    def calendar_appointment_create(self, appointment_id=None, **post):
        if appointment_id:
            appt = request.env['calendar.appointment'].sudo().browse(int(appointment_id))
            if appt and appt.appointment_tz:
                post['timezone'] = appt.appointment_tz
        return super(WebsiteCalendarTZLock, self).calendar_appointment_create(
            appointment_id=appointment_id, **post
        )
