from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class Branch(models.Model):
    _name = 'branch.branch'
    _description = 'Branch'
    _order = 'name'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Branch Name', required=True, tracking=True)
    code = fields.Char(string='Branch Code', tracking=True)
    manager_id = fields.Many2one('res.users', string='Branch Manager', tracking=True)
    active = fields.Boolean(default=True, tracking=True)
    
    # Smart buttons fields
    user_count = fields.Integer(compute='_compute_counts', string='Users')
    partner_count = fields.Integer(compute='_compute_counts', string='Customers')
    employee_count = fields.Integer(compute='_compute_counts', string='Employees')
    lead_count = fields.Integer(compute='_compute_counts', string='Leads')
    event_count = fields.Integer(compute='_compute_counts', string='Events')
    
    @api.depends('name', 'manager_id')
    def _compute_counts(self):
        for branch in self:
            branch.user_count = self.env['res.users'].search_count([('branch_id', '=', branch.id)])
            branch.partner_count = self.env['res.partner'].search_count([('branch_id', '=', branch.id)])
            branch.employee_count = self.env['hr.employee'].search_count([('branch_id', '=', branch.id)])
            branch.lead_count = self.env['crm.lead'].search_count([('branch_id', '=', branch.id)])
            branch.event_count = self.env['calendar.event'].search_count([('branch_id', '=', branch.id)])

    @api.constrains('manager_id')
    def _check_manager(self):
        for branch in self:
            if branch.manager_id and branch.manager_id.branch_id != branch:
                raise ValidationError(_('The branch manager must be assigned to this branch.'))

    def action_view_users(self):
        return {
            'name': _('Users'),
            'type': 'ir.actions.act_window',
            'res_model': 'res.users',
            'view_mode': 'tree,form',
            'domain': [('branch_id', '=', self.id)],
            'context': {'create': False},
        }

    def action_view_partners(self):
        return {
            'name': _('Customers'),
            'type': 'ir.actions.act_window',
            'res_model': 'res.partner',
            'view_mode': 'tree,form',
            'domain': [('branch_id', '=', self.id)],
            'context': {'create': False},
        }

    def action_view_employees(self):
        return {
            'name': _('Employees'),
            'type': 'ir.actions.act_window',
            'res_model': 'hr.employee',
            'view_mode': 'tree,form',
            'domain': [('branch_id', '=', self.id)],
            'context': {'create': False},
        }

    def action_view_leads(self):
        return {
            'name': _('Leads'),
            'type': 'ir.actions.act_window',
            'res_model': 'crm.lead',
            'view_mode': 'tree,form',
            'domain': [('branch_id', '=', self.id)],
            'context': {'create': False},
        }

    def action_view_events(self):
        return {
            'name': _('Events'),
            'type': 'ir.actions.act_window',
            'res_model': 'calendar.event',
            'view_mode': 'calendar,tree,form',
            'domain': [('branch_id', '=', self.id)],
            'context': {'create': False},
        } 