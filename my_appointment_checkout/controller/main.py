from odoo import http
from odoo import http
from odoo.http import request

class WebsiteAppointmentSale(http.Controller):

    @http.route(['/calendar/appointment/create', '/calendar/appointment/confirm'],
                type='http', auth="public", website=True, methods=['POST'], csrf=False)
    def calendar_appointment_create(self, **post):
        # 1) Kreiranje/izmena partnera
        vals = {
            'name': post.get('name'),
            'email': post.get('email'),
            'phone': post.get('phone'),
        }
        partner = request.env['res.partner'].sudo().search([('email','=',vals['email'])], limit=1)
        if not partner:
            partner = request.env['res.partner'].sudo().create(vals)
        else:
            partner.sudo().write(vals)

        # 2) Veza na sale.order u sessiji
        order = request.website.sale_get_order(force_create=True)
        order.sudo().write({
            'partner_id': partner.id,
            'partner_invoice_id': partner.id,
            'partner_shipping_id': partner.id,
        })

        # 3) Redirect na payment (zaobiđi checkout)
        return request.redirect('/shop/payment')
