from odoo import models, api, fields
from datetime import datetime, timedelta

class MailMessage(models.Model):
    _inherit = 'mail.message'

    @api.model_create_multi
    def create(self, vals_list):
        messages = super().create(vals_list)
        for message in messages:
            if message.author_id and message.model == 'im_livechat.channel':
                message.author_id.last_activity_time = fields.Datetime.now()
        return messages
