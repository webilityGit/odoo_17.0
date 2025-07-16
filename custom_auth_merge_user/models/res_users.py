import logging
from odoo import api, models

_logger = logging.getLogger(__name__)

class ResUsers(models.Model):
    _inherit = 'res.users'

    @api.model
    def _signup_create_user(self, values):
        """
        Hook signup to merge duplicate partners based on email.
        """
        _logger.info('>>> appointment_auth_merge: signup hook values=%s', values)
        user = super(ResUsers, self)._signup_create_user(values)

        partner = user.partner_id
        if partner and partner.email:
            # find duplicates only by email
            dup = self.env['res.partner'].sudo().search([
                ('email','=', partner.email),
                ('id','!=', partner.id),
            ])
            if dup:
                wiz = self.env['base.partner.merge.automatic.wizard'].sudo().create({
                    'merge_mode': 'manual',
                    'dst_partner_id': partner.id,
                })
                wiz.write({'partner_ids': [(6, 0, dup.ids + [partner.id])]})
                wiz.merge_action()

        return user