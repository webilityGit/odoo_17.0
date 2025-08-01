from odoo import api, fields, models
from datetime import timedelta

class BusPresence(models.Model):
    _inherit = 'bus.presence'

    @api.model
    def _update_presence(self, inactivity_period, identity_field, identity_value):
        """Override default timeout logic to extend Live Chat operator session duration."""
        # Default timeout: 30 minutes in ms
        default_timeout = 30 * 60 * 1000
        # Extended timeout: 4 hours in ms
        extended_timeout = 4 * 60 * 60 * 1000

        # ✅ Ispravna provera da li je user Live Chat operater
        is_livechat_operator = self.env['im_livechat.operator'].sudo().search_count([
            ('user_id', '=', identity_value)
        ]) > 0

        timeout_limit = extended_timeout if is_livechat_operator else default_timeout

        presence = self.search([(identity_field, '=', identity_value)])
        values = {
            "last_poll": fields.Datetime.now(),
            "last_presence": fields.Datetime.now() - timedelta(milliseconds=inactivity_period),
            "status": "away" if inactivity_period > timeout_limit else "online",
        }

        if not presence:
            values[identity_field] = identity_value
            presence = self.create(values)
        else:
            presence.write(values)
