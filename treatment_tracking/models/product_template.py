from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    treatment_type_id = fields.Many2one(
        'treatment.type',
        string='סוג הטיפול',
        help='סוג הטיפול הקשור למוצר זה'
    ) 