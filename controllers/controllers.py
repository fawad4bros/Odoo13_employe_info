# -*- coding: utf-8 -*-
from odoo import http


class EmployeInfo(http.Controller):
    @http.route('/employe_info/employe_info/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/employe_info/employe_info/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('employe_info.listing', {
            'root': '/employe_info/employe_info',
            'objects': http.request.env['employe_info.employe_info'].search([]),
        })

    @http.route('/employe_info/employe_info/objects/<model("employe_info.employe_info"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('employe_info.object', {
            'object': obj
        })
