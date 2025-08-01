from odoo import models, api, fields
from datetime import datetime, timedelta

class MailMessage(models.Model):
    _inherit = 'mail.message'

    @api.model
    def create(self, vals):
        message = super().create(vals)
        if message.author_id and message.model == 'im_livechat.channel':
            message.author_id.last_activity_time = fields.Datetime.now()
        return message
