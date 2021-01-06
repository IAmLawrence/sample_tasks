# -*- coding: utf-8 -*-
from odoo import http

# class EventRegistration(http.Controller):
#     @http.route('/event_registration/event_registration/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/event_registration/event_registration/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('event_registration.listing', {
#             'root': '/event_registration/event_registration',
#             'objects': http.request.env['event_registration.event_registration'].search([]),
#         })

#     @http.route('/event_registration/event_registration/objects/<model("event_registration.event_registration"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('event_registration.object', {
#             'object': obj
#         })