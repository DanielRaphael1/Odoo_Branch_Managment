from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    calendar_event_ids = fields.One2many(
        'calendar.event',
        'partner_ids',
        string='אירועים'
    )

    completed_treatment_count = fields.Integer(
        string='מספר טיפולים שהושלמו',
        compute='_compute_completed_treatment_count'
    )

    @api.depends('calendar_event_ids.treatment_done')
    def _compute_completed_treatment_count(self):
        for partner in self:
            partner.completed_treatment_count = self.env['calendar.event'].search_count([
                ('partner_ids', 'in', partner.id),
                ('treatment_done', '=', True)
            ])

    def action_view_completed_treatments(self):
        self.ensure_one()
        return {
            'name': 'טיפולים שהושלמו',
            'type': 'ir.actions.act_window',
            'res_model': 'calendar.event',
            'view_mode': 'list,form',
            'domain': [
                ('partner_ids', 'in', self.id),
                ('treatment_done', '=', True)
            ],
            'context': {'create': False}
        } 