# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Collection(models.Model):
    _name = 'stories.collection'

    name = fields.Char(
        string='Name',
        help='Name of the collection'
    )

    launch_date = fields.Date(
        string='Launch date',
        help='Launch date of the collection.'
    )


class Story(models.Model):
    _name = 'stories.story'

    serial = fields.Many2one(
        string='Serial code',
        help='Serial code associated with this story.'
    )

    story = fields.Text(
        string='Story',
        help='Personal story of an owner of this garment.'
    )

    user = fields.Many2one(
        string='User',
        help='User that owns the associated garment and story.',
        comodel_name='res.users',
        ondelete='set null'
    )


class Serial(models.Model):
    _name = 'stories.serial'

    code = fields.Char(
        string='Serial code',
        help='Unique serial code for a garment in a collection.'
    )

    collection = fields.Many2one(
        string='Collection',
        help='Rucca collection associated with this serial.',
        comodel_name='stories.collection',
        ondelete='set null'
    )
