# -*- coding: utf-8 -*-
# from odoo import http


# class VztProject(http.Controller):
#     @http.route('/vzt_project/vzt_project/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vzt_project/vzt_project/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vzt_project.listing', {
#             'root': '/vzt_project/vzt_project',
#             'objects': http.request.env['vzt_project.vzt_project'].search([]),
#         })

#     @http.route('/vzt_project/vzt_project/objects/<model("vzt_project.vzt_project"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vzt_project.object', {
#             'object': obj
#         })
