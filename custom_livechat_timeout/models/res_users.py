from odoo import models
from datetime import datetime, timedelta

class ResUsers(models.Model):
    _inherit = 'res.users'

    def _extend_livechat_presence(self):
        """Extend activity timeout for Live Chat operators."""
        now = datetime.utcnow()
        presence_model = self.env['bus.presence']

        active_operator_ids = self.env['im_livechat.channel'].search([]).mapped('user_ids').ids
        for user_id in active_operator_ids:
            presence = presence_model.sudo().search([('user_id', '=', user_id)], limit=1)
            if presence:
                presence.sudo().write({
                    'last_poll': now.strftime('%Y-%m-%d %H:%M:%S'),
                })
