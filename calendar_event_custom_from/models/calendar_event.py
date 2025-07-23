# -*- coding: utf-8 -*-
from odoo import models, api

class CalendarEvent(models.Model):
    _inherit = "calendar.event"


    def message_post(self, *args, **kwargs):
        # Ako već nije prosleđeno, postavi željeni From:
        default_from = "Winera Bookings <bookings@winera.com>"
        kwargs.setdefault("email_from", default_from)

        # (Opcionalno) Prosledi mail_server_id ako želiš usmeriti na specifičan SMTP:
        # server = self.env.ref("your_module.ir_mail_server_custom", raise_if_not_found=False)
        # if server:
        #     kwargs.setdefault("mail_server_id", server.id)

        return super(CalendarEvent, self).message_post(*args, **kwargs)
