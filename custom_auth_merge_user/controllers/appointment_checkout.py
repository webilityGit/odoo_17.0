from odoo import http
from odoo.http import request

class WebsiteAppointmentCheckout(http.Controller):
    @http.route([
        '/calendar/appointment/create',
        '/calendar/appointment/confirm',
    ], type='http', auth='public', website=True, methods=['POST'], csrf=False)
    def calendar_appointment_create(self, **post):
        # 1) Create or update partner safely
        vals = {
            'name': post.get('name'),
            'email': post.get('email'),
            'phone': post.get('phone'),
        }
        Partner = request.env['res.partner'].sudo()
        partner = Partner.search([('email','=', vals['email'])], limit=1)
        if not partner:
            partner = Partner.create(vals)
        else:
            partner.write(vals)

        # 2) Bind partner to sale.order under sudo() to avoid ACL
        order = request.website.sale_get_order(force_create=True).sudo()
        order.write({
            'partner_id': partner.id,
            'partner_invoice_id': partner.id,
            'partner_shipping_id': partner.id,
        })

        # 3) Render confirmation or redirect as needed
        return request.render('appointment_auth_merge.appointment_confirmation', {
            'order': order,
            'partner': partner,
        })