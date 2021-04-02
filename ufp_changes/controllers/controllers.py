# -*- coding: utf-8 -*-
# from odoo import http


# class UfpChanges(http.Controller):
#     @http.route('/ufp_changes/ufp_changes/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ufp_changes/ufp_changes/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ufp_changes.listing', {
#             'root': '/ufp_changes/ufp_changes',
#             'objects': http.request.env['ufp_changes.ufp_changes'].search([]),
#         })

#     @http.route('/ufp_changes/ufp_changes/objects/<model("ufp_changes.ufp_changes"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ufp_changes.object', {
#             'object': obj
#         })
