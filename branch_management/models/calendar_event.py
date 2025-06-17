from odoo import models, fields, api

class CalendarEvent(models.Model):
    _inherit = 'calendar.event'

    branch_id = fields.Many2one('branch.branch', string='Branch',
        default=lambda self: self.env.user.branch_id,
        tracking=True,
        index=True) 