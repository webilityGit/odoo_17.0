from odoo import models, fields

class AppointmentPrebook(models.Model):
    _name = 'appointment.prebook'
    _description = 'Appointment Pre-book Log'

    slot_id = fields.Integer(string='Slot ID', required=True)
    visitor_id = fields.Char(string='Visitor Session ID')
    action = fields.Selection(
        [('view', 'View'), ('confirm', 'Confirm'), ('cancel', 'Cancel')],
        string='Action', required=True
    )
    info = fields.Text(string='Form Data (JSON)')
    create_date = fields.Datetime(string='Timestamp', readonly=True, default=lambda self: fields.Datetime.now())