from odoo import models, fields, api
from odoo.exceptions import UserError
import logging

_logger = logging.getLogger(__name__)

class CalendarEvent(models.Model):
    _inherit = 'calendar.event'

    treatment_type_id = fields.Many2one(
        'treatment.type',
        string='סוג הטיפול'
    )
    treatment_done = fields.Boolean(
        string='טיפול הושלם',
        default=False
    )
    sale_order_line_id = fields.Many2one(
        'sale.order.line',
        string='שורת הזמנה',
        readonly=True
    )
    invoice_id = fields.Many2one(
        'account.move',
        string='חשבונית',
        readonly=True
    )

    def action_mark_treatment_done(self):
        self.ensure_one()
        if not self.partner_ids:
            raise UserError('יש לציין לקוח לאירוע')
        
        if not self.treatment_type_id:
            raise UserError('יש לציין סוג טיפול לאירוע')

        # Get the first partner (main customer)
        partner = self.partner_ids[0]
        _logger.info(f'Processing treatment for partner: {partner.name}')

        # Find matching sale order line
        sale_line = self.env['sale.order.line'].search([
            ('order_id.partner_id', '=', partner.id),
            ('treatment_type_id', '=', self.treatment_type_id.id),
            ('remaining_treatments', '>', 0),
            ('order_id.state', 'in', ['sale', 'done'])
        ], order='create_date desc', limit=1)

        if not sale_line:
            raise UserError('לא נמצאה הזמנה מתאימה עם טיפולים נותרים')

        _logger.info(f'Found sale order line: {sale_line.id} from order {sale_line.order_id.name}')

        # Update sale order line
        sale_line.treatments_completed += 1
        self.sale_order_line_id = sale_line.id

        try:
            # Create invoice
            invoice = self._create_treatment_invoice(sale_line, partner)
            self.invoice_id = invoice.id
            _logger.info(f'Created invoice: {invoice.name}')

            # Mark treatment as done
            self.treatment_done = True

            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': 'הצלחה',
                    'message': f'הטיפול סומן כהושלם והחשבונית {invoice.name} נוצרה בהצלחה',
                    'type': 'success',
                    'sticky': False,
                }
            }
        except Exception as e:
            _logger.error(f'Error creating invoice: {str(e)}')
            raise UserError(f'שגיאה ביצירת חשבונית: {str(e)}')

    def _create_treatment_invoice(self, sale_line, partner):
        try:
            # Create invoice
            invoice_vals = {
                'partner_id': partner.id,
                'move_type': 'out_invoice',
                'invoice_line_ids': [(0, 0, {
                    'product_id': sale_line.product_id.id,
                    'quantity': 1,
                    'price_unit': sale_line.price_unit,
                    'name': f'טיפול: {self.treatment_type_id.name}',
                    'account_id': sale_line.product_id.property_account_income_id.id or sale_line.product_id.categ_id.property_account_income_categ_id.id,
                })],
            }
            _logger.info(f'Creating invoice with vals: {invoice_vals}')
            
            invoice = self.env['account.move'].create(invoice_vals)
            _logger.info(f'Created invoice: {invoice.name}')
            
            # Post the invoice
            invoice.action_post()
            _logger.info(f'Posted invoice: {invoice.name}')

            return invoice
        except Exception as e:
            _logger.error(f'Error in _create_treatment_invoice: {str(e)}')
            raise 