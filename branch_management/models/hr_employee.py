from odoo import models, fields, api

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    branch_id = fields.Many2one('branch.branch', string='Branch',
        tracking=True,
        index=True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('branch_id'):
                vals['branch_id'] = self.env.user.branch_id.id
        return super().create(vals_list) 