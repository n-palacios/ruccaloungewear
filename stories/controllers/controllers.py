# -*- coding: utf-8 -*-
from odoo import http

class MyModule(http.Controller):
    @http.route('/stories/collection/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/stories/collection/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('stories.collection', {
            'root': '/stories/collection',
            'objects': http.request.env['stories.collection'].search([]),
        })

    @http.route('/stories/collection/objects/<model("stories.collection"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('stories.object', {
            'object': obj
        })