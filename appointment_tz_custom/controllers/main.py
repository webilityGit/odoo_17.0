from odoo.addons.enterprise.appointment.controllers.appointment import AppointmentController

class AppointmentControllerTZ(AppointmentController):
    # override the helper that picks your default TZ
    def _get_default_timezone(self, appointment_type):
        # always use the tz configured on the appointment type
        return appointment_type.appointment_tz

    # no need to override _get_appointment_type_page_view
    # because it will pick up request.session.timezone = this value
