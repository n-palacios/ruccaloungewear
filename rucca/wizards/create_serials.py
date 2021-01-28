from odoo import models, api

class CreateSerials(models.TransientModel):
    _name = 'create.serials'

    number = fields.Integer(string="How many serial codes to create?")