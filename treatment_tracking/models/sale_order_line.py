from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    treatment_type_id = fields.Many2one(
        'treatment.type',
        string='סוג הטיפול',
        compute='_compute_treatment_type',
        store=True
    )
    treatments_completed = fields.Integer(
        string='טיפולים שהושלמו',
        default=0
    )
    remaining_treatments = fields.Integer(
        string='טיפולים נותרו',
        compute='_compute_remaining_treatments',
        store=True
    )

    @api.depends('product_id.treatment_type_id')
    def _compute_treatment_type(self):
        for line in self:
            line.treatment_type_id = line.product_id.treatment_type_id

    @api.depends('product_uom_qty', 'treatments_completed')
    def _compute_remaining_treatments(self):
        for line in self:
            line.remaining_treatments = line.product_uom_qty - line.treatments_completed 