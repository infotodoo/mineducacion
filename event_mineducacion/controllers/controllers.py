# -*- coding: utf-8 -*-
from odoo import http

# class EventMineducacion(http.Controller):
#     @http.route('/event_mineducacion/event_mineducacion/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/event_mineducacion/event_mineducacion/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('event_mineducacion.listing', {
#             'root': '/event_mineducacion/event_mineducacion',
#             'objects': http.request.env['event_mineducacion.event_mineducacion'].search([]),
#         })

#     @http.route('/event_mineducacion/event_mineducacion/objects/<model("event_mineducacion.event_mineducacion"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('event_mineducacion.object', {
#             'object': obj
#         })