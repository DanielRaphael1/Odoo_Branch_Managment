from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ResUsers(models.Model):
    _inherit = 'res.users'

    branch_id = fields.Many2one('branch.branch', string='Branch', tracking=True)
    
    @api.constrains('branch_id')
    def _check_branch_manager(self):
        for user in self:
            if user.branch_id and user.branch_id.manager_id and user.branch_id.manager_id != user:
                if user.has_group('branch_management.group_branch_manager'):
                    raise ValidationError('A branch can only have one manager.') 