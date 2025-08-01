from odoo import models, api, fields

class LivechatChannel(models.Model):
    _inherit = 'im_livechat.channel'

    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)
        for record in records:
            if record.livechat_channel_id:
                for user in record.livechat_channel_id.user_ids:
                    user.notify_info(
                        message="Novi live chat je započet putem sajta.",
                        title="Live Chat Notifikacija",
                        sticky=True
                    )
        return records
