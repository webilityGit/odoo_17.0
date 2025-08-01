from odoo import models

class BusPresence(models.Model):
    _inherit = 'bus.presence'

    def _update_presence(self, inactivity_period=3600, identity_field='user_id', identity_value=None):
        # Produženo sa 30 minuta (1800 sekundi) na 6 sati (21600 sekundi)
        return super()._update_presence(inactivity_period=21600, identity_field=identity_field, identity_value=identity_value)
