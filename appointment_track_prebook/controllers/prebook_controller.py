from odoo import http
from odoo.http import request
import json

class PrebookController(http.Controller):
    @http.route(
        '/appointment/<int:slot_id>/action/<string:action>',
        type='http', auth='public', website=True, methods=['POST'], csrf=False
    )
    def appointment_action(self, slot_id, action, **post):
        Prebook = request.env['appointment.prebook'].sudo()
        visitor = request.session.get('visitor_id')
        Prebook.create({
            'slot_id': slot_id,
            'visitor_id': visitor,
            'action': action,
            'info': json.dumps(post),
        })
        # call standard Odoo website_appointment controller
        return super(PrebookController, self).appointment_action(slot_id, action, **post)