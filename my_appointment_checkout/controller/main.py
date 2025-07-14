from odoo import http
from odoo.http import request

class WebsiteAppointmentSale(http.Controller):

    @http.route(['/appointment/confirm'], type='http', auth="public", website=True, methods=['POST'], csrf=False)
    def appointment_confirm(self, **post):
        # 1. Prepare partner values
        partner_vals = {
            'name': post.get('name'),
            'email': post.get('email'),
            'phone': post.get('phone'),
        }
        # 2. Find or create partner
        partner = request.env['res.partner'].sudo().search([('email', '=', partner_vals['email'])], limit=1)
        if not partner:
            partner = request.env['res.partner'].sudo().create(partner_vals)
        else:
            partner.sudo().write(partner_vals)

        # 3. Assign to sale.order
        order = request.website.sale_get_order(force_create=True)
        order.sudo().write({
            'partner_id': partner.id,
            'partner_invoice_id': partner.id,
            'partner_shipping_id': partner.id,
        })

        # 4. (Optional) add product or participants to order
        # order.sudo()._cart_update(
        #     product_id=int(post['product_id']),
        #     product_uom_qty=int(post['participants']),
        # )

        # 5. Redirect to payment, skipping address
        return request.redirect('/shop/payment')