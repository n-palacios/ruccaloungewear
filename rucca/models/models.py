# -*- coding: utf-8 -*-

from odoo import models, fields, api



class Collection(models.Model):
    _name = 'rucca.collection'
    _description = 'Collection of loungewear.'

    name = fields.Char(
        string='Name',
        help='Name of the collection'
    )

    description = fields.Text(
        string='Description',
        help='Detailed src of the collection.'
    )

    launch_date = fields.Date(
        string='Launch date',
        help='Launch date of the collection.',
        default=fields.Date.today()
    )


class Story(models.Model):
    _name = 'rucca.story'
    _description = 'Textual story of each user associated with a purchased unit.'

    serial = fields.Many2one(
        string='Serial code',
        help='Serial code associated with this story.',
        comodel_name='rucca.serial',
        ondelete='restrict',
        required=True
    )

    user = fields.Many2one(
        string='User',
        help='User that owns the associated garment and story.',
        comodel_name='res.users',
        ondelete='cascade',
        required=True,
        default=lambda self: self.env.user
    )

    story = fields.Text(
        string='Story',
        help='Personal story of an owner of this garment.'
    )


class Serial(models.Model):
    _name = 'rucca.serial'
    _description = 'Serial code associated with a collection.'
    _sql_constraints = [
        ('name_unique', 'unique(name)', 'No puedes crear dos números de serie iguales!')
        ]

    name = fields.Char(
        string='Serial code',
        help='Unique serial code for a garment in a collection.',
        required=True
    )

    collection = fields.Many2one(
        string='Collection',
        help='Rucca collection associated with this serial.',
        comodel_name='rucca.collection',
        ondelete='restrict',
        required=True
    )

# class ProductTemplate(models.Model):
#     _inherit = 'product.template'
#
#     collection = fields.Many2one(
#         string='Collection',
#         help='Rucca collection associated with this serial.',
#         comodel_name='rucca.collection',
#         ondelete='set null'
#     )


