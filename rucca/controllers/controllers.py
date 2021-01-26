# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request


class RuccaController(http.Controller):
    @http.route('/create_story/rucca.story', auth='user', website=True)
    def index(self, **kw):
        # necessary fields for a story

        serials = request.env['rucca.serial'].search(['name', '=', kw['Número de Serie']])

        if not serials:
            return {'warning': {
                'title': ('Advertencia'),
                'message': ('El número serial ingresado no existe.')}
            }
        else:
            kw['serial'] = serials
            kw['story'] = kw['Tu Historia']

        # create the story
        request.env['rucca.story'].sudo().create(kw)
