from odoo import http
from odoo.http import request
import json

# Nasleđujemo originalni WebsiteAppointment
from odoo.addons.website_appointment.controllers.main import WebsiteAppointment

class PrebookController(WebsiteAppointment):

    # 1) Logujemo kada korisnik *prikazuje* termin
    @http.route(
        ['/calendar/appointment/<model("calendar.slot"):slot>'],
        type='http', auth='public', website=True, methods=['GET'], csrf=False)
    def appointment_slot(self, slot, **kw):
        request.env['appointment.prebook'].sudo().create({
            'slot_id': slot.id,
            'visitor_id': request.session.get('visitor_id'),
            'action': 'view',
            'info': json.dumps({'params': kw}),
        })
        return super().appointment_slot(slot, **kw)

    # 2) Logujemo kada korisnik *potvrdi* termin
    @http.route([
        '/calendar/appointment/create',
        '/calendar/appointment/confirm',
    ], type='http', auth='public', website=True, methods=['POST'], csrf=False)
    def calendar_appointment_create(self, **post):
        slot_id = post.get('slot_id') or post.get('appointment_slot_id')
        if slot_id:
            request.env['appointment.prebook'].sudo().create({
                'slot_id': int(slot_id),
                'visitor_id': request.session.get('visitor_id'),
                'action': 'confirm',
                'info': json.dumps(post),
            })
        return super().calendar_appointment_create(**post)