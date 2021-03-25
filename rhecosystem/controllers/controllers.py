# -*- coding: utf-8 -*-
# from odoo import http


# class Rhecosystem(http.Controller):
#     @http.route('/rhecosystem/rhecosystem/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rhecosystem/rhecosystem/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rhecosystem.listing', {
#             'root': '/rhecosystem/rhecosystem',
#             'objects': http.request.env['rhecosystem.rhecosystem'].search([]),
#         })

#     @http.route('/rhecosystem/rhecosystem/objects/<model("rhecosystem.rhecosystem"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rhecosystem.object', {
#             'object': obj
#         })
