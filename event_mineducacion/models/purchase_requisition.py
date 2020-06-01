# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PurchaseRequisition(models.Model):
    _inherit = 'purchase.requisition'

    @api.depends('line_ids.price_total')
    def _amount_all(self):
        for requisition in self:
            amount_untaxed = amount_tax = 0.0
            for line in requisition.line_ids:
                amount_untaxed += line.price_subtotal
                amount_tax += line.price_tax
            requisition.update({
                'amount_untaxed': requisition.currency_id.round(amount_untaxed),
                'amount_tax': requisition.currency_id.round(amount_tax),
                'amount_total': amount_untaxed + amount_tax,
            })

    amount_untaxed = fields.Monetary(string='Untaxed Amount', store=True, readonly=True, compute='_amount_all', track_visibility='always')
    amount_tax = fields.Monetary(string='Taxes', store=True, readonly=True, compute='_amount_all')
    amount_total = fields.Monetary(string='Total', store=True, readonly=True, compute='_amount_all')


class PurchaseRequisitionLine(models.Model):
    _inherit = 'purchase.requisition.line'

    @api.depends('product_qty', 'price_unit', 'taxes_id')
    def _compute_amount(self):
        for line in self:
            vals = line._prepare_compute_all_values()
            taxes = line.taxes_id.compute_all(
                vals['price_unit'],
                vals['currency_id'],
                vals['product_qty'],
                vals['product'],
                vals['partner'])
            line.update({
                'price_tax': sum(t.get('amount', 0.0) for t in taxes.get('taxes', [])),
                'price_total': taxes['total_included'],
                'price_subtotal': taxes['total_excluded'],
            })

    # Related 
    # partner_id = fields.Many2one('res.partner', related='requisition_id.vendor_id', string='Partner', readonly=True, store=True)
    currency_id = fields.Many2one('res.currency', related='requisition_id.currency_id', store=True, string='Currency', readonly=True)

    taxes_id = fields.Many2many('account.tax', string='Taxes', domain=['|', ('active', '=', False), ('active', '=', True)])
    price_subtotal = fields.Monetary(compute='_compute_amount', string='Subtotal', store=True, currency_field='currency_id')
    price_total = fields.Monetary(compute='_compute_amount', string='Total', store=True)
    price_tax = fields.Float(compute='_compute_amount', string='Tax', store=True)

    def _prepare_compute_all_values(self):
        self.ensure_one()
        return {
            'price_unit': self.price_unit,
            'currency_id': self.requisition_id.currency_id,
            'product_qty': self.product_qty,
            'product': self.product_id,
            'partner': self.requisition_id.vendor_id,
        }
