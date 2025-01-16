from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.http import request


class CustomWebsiteSale(WebsiteSale):
    def shop(self, page=0, category=None, search='', min_price=0.0, max_price=0.0, ppg=False, **post):
        # Call the super method to inherit its behavior
        response = super(CustomWebsiteSale, self).shop(
            page=page, category=category, search=search,
            min_price=min_price, max_price=max_price, ppg=ppg, **post
        )

        ProductAttribute = request.env['product.attribute']
        att = ProductAttribute.search([('name', 'ilike', 'Continents')])
        request_args = request.httprequest.args
        attrib_list = request_args.getlist('attribute_value')
        attrib_values = [[int(x) for x in v.split("-")] for v in attrib_list if v]
        attributes_ids = {v[0] for v in attrib_values}
        attrib_set = {v[1] for v in attrib_values}

        single_attributes_values = request.env['product.attribute.value'].browse(attrib_set)

        att_list = [att.id]
        if attrib_values:
            att_list += ProductAttribute.search([
                ('name', 'in', single_attributes_values.mapped('name'))
            ]).ids
        attributes = ProductAttribute.search([('id', 'in', att_list)])

        if hasattr(response, 'qcontext'):
            response.qcontext['attributes'] = attributes

        return response
