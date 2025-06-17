from odoo import models, fields, api

class TreatmentType(models.Model):
    _name = 'treatment.type'
    _description = 'Treatment Type'
    _order = 'name'

    name = fields.Char(string='שם הטיפול', required=True)
    active = fields.Boolean(default=True)
    description = fields.Text(string='תיאור')
    
    _sql_constraints = [
        ('name_uniq', 'unique(name)', 'שם הטיפול חייב להיות ייחודי!')
    ] 