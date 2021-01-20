# -*- coding: utf-8 -*-
{
    'name': "Rucca Stories",

    'summary': """
        Stories, collections, and serial codes manaement app for Rucca Loungewear""",

    'src': """
        Stories, collections, and serial codes manaement app for Rucca Loungewear.
    """,

    'author': "Prizma Consulting",
    'website': "http://www.prizmaconsulting.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'application': True,
    'installable': True,
}