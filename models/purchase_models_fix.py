from openerp import api, fields, models


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    @api.multi
    def button_dummy(self):
        self.write({'state': 'draft'})
        for line in self.order_line:
            line._onchange_quantity()
            if line.product_qty <= 0:
                self.order_line -= line
