# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request


class RuccaController(http.Controller):
    @http.route('/create_story/', auth='user', website=True)
    def index(self, **kw):
        # necessary fields for a story
        raise Exception(kw)
        serials = request.env['rucca.serial'].search(['name', '=', kw['serial']])

        if not serials:
            return {'warning': {
                'title': ('Advertencia'),
                'message': ('El número serial ingresado no existe.')}
            }
        else:
            kw['serial'] = serials

        # create the story
        request.env['rucca.story'].sudo().create(kw)
