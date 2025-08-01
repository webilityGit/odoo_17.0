from odoo import models, api, fields
from datetime import datetime, timedelta

class ResUsers(models.Model):
    _inherit = 'res.users'

    last_activity_time = fields.Datetime(string="Last Livechat Activity", default=fields.Datetime.now)

    @api.model
    def notify_inactive_operators(self):
        threshold_hours = 3  # Promeni na 4 ako treba
        now = fields.Datetime.now()
        cutoff = now - timedelta(hours=threshold_hours)

        internal_users = self.search([('share', '=', False)])
        for user in internal_users:
            if not user.last_activity_time or user.last_activity_time < cutoff:
                user.notify_info(
                    message="Novi chat je započet, a niste bili aktivni preko {}h.".format(threshold_hours),
                    title="Podsetnik za Live Chat",
                    sticky=True
                )