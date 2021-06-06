# -*- coding: utf-8 -*-

# noinspection PyUnresolvedReferences
from odoo import models, fields, api

class Facturacion(models.Model):
	_inherit = 'account.move'
	def send_and_print_action(self,values):
		res = super(Facturacion, self).send_and_print_action(values)
		raise Exception('mensaje de prueba')

	