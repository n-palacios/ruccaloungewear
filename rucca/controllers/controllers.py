# -*- coding: utf-8 -*-
from odoo import http

class MyModule(http.Controller):
    @http.route('/rucca/collection/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/rucca/collection/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('rucca.listing', {
            'root': '/rucca/collection',
            'objects': http.request.env['rucca.collection'].search([]),
        })

    @http.route('/rucca/collection/objects/<model("rucca.collection"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('rucca.object', {
            'object': obj
        })