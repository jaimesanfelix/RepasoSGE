# -*- coding: utf-8 -*-
# from odoo import http


# class Agricultores(http.Controller):
#     @http.route('/agricultores/agricultores', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/agricultores/agricultores/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('agricultores.listing', {
#             'root': '/agricultores/agricultores',
#             'objects': http.request.env['agricultores.agricultores'].search([]),
#         })

#     @http.route('/agricultores/agricultores/objects/<model("agricultores.agricultores"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('agricultores.object', {
#             'object': obj
#         })
