from odoo import models, api, fields
from datetime import datetime, timedelta

class LivechatChannelSession(models.Model):
    _inherit = 'im_livechat.channel.session'

    @api.model
    def create(self, vals):
        session = super().create(vals)
        if session.livechat_channel_id:
            operators = session.livechat_channel_id.user_ids
            for user in operators:
                user.notify_info(
                    message="Novi live chat je započet putem sajta.",
                    title="Live Chat Notifikacija",
                    sticky=True
                )
        return session