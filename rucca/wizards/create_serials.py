from odoo import models, api, fields

class CreateSerials(models.TransientModel):
    _name = 'create.serials'

    number = fields.Integer(string="How many serial codes to create?")

    def create_serials(self):
        for i in range(self.number):
            pass