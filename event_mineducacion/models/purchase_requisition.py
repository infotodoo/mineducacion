# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PurchaseRequisition(models.Model):
    _inherit = 'purchase.requisition'

    @api.depends('line_ids.price_unit')
    def _amount_all(self):
        for order in self:
            amount_total = 0.0
            for line in order.line_ids:
                amount_total += line.price_unit
            order.update({
                'amount_total': amount_total,
            })

    amount_total = fields.Monetary(string='Total', store=True, readonly=True, compute='_amount_all')
