# -*- coding: utf-8 -*-

from odoo import models, fields, api


class EventEvent(models.Model):
    _inherit = 'event.event'

    analytic_id = fields.Many2one('account.analytic.account', 'Analytic account')
    requisition_id = fields.Many2one('purchase.requisition', 'Requisition')
