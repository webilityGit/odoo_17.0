from odoo import api, models

class ResUsers(models.Model):
    _inherit = 'res.users'

    @api.model
    def _signup_create_user(self, values):
        """
        Override to merge duplicate partners based on email+phone
        whenever a new user is created via signup.
        """
        # 1) Call core logic to create user and partner
        user = super(ResUsers, self)._signup_create_user(values)

        # 2) Merge partners with same email and phone
        partner = user.partner_id
        if partner and partner.email and partner.phone:
            dup = self.env['res.partner'].sudo().search([
                ('email', '=', partner.email),
                ('phone', '=', partner.phone),
                ('id', '!=', partner.id),
            ])
            if dup:
                # Use the correct wizard model name from base module
                wizard = self.env['base.partner.merge.automatic.wizard'].sudo().create({
                    'merge_mode': 'manual',
                    'dst_partner_id': partner.id,
                })
                wizard.write({
                    'partner_ids': [(6, 0, dup.ids + [partner.id])]
                })
                wizard.merge_action()

        # 3) Return the created user
        return user