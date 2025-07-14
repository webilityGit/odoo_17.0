# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
# OVDE ide import bazne klase, odmah ispod ostalih
from odoo.addons.website_sale.controllers.main import WebsiteSale as _WebsiteSale

class WebsiteAppointmentSale(http.Controller):

    @http.route([
        '/calendar/appointment/create',
        '/calendar/appointment/confirm',
    ], type='http', auth='public', website=True, methods=['POST'], csrf=False)
    def calendar_appointment_create(self, **post):
        # 1. Create or update partner
        vals = {
            'name': post.get('name'),
            'email': post.get('email'),
            'phone': post.get('phone'),
        }
        Partner = request.env['res.partner'].sudo()
        partner = Partner.search([('email', '=', vals['email'])], limit=1)
        if not partner:
            partner = Partner.create(vals)
        else:
            partner.write(vals)

        # 2. Bind partner to sale.order in session
        order = request.website.sale_get_order(force_create=True)
        order.sudo().write({
            'partner_id': partner.id,
            'partner_invoice_id': partner.id,
            'partner_shipping_id': partner.id,
        })

        # 3. Redirect straight to payment
        return request.redirect('/shop/payment')


class WebsiteShopSkipAddress(http.Controller):

    @http.route([
        '/shop/checkout',
        '/shop/address',
    ], type='http', auth='public', website=True, sitemap=False)
    def skip_address(self, **post):
        order = request.website.sale_get_order()
        if order and order.partner_id:
            # Skip address if partner already set
            return request.redirect('/shop/payment')
        # Otherwise normal checkout
        return request.redirect('/shop/checkout')


class WebsiteShopPaymentSkip(_WebsiteSale):

    @http.route(['/shop/payment'], type='http', auth='public', website=True, sitemap=False)
    def payment(self, transaction=None, **post):
        # Fetch current sale order
        order = request.website.sale_get_order()
        if not order or not order.order_line:
            return request.redirect('/shop')
        # Directly render payment template
        values = self._get_payment_values(order, transaction)
        values.update({
            'order': order,
        # 'use_delivery_as_billing' is also used in address_on_payment:
            'use_delivery_as_billing': order.partner_shipping_id == order.partner_invoice_id,
        })
        return request.render("website_sale.payment", values)