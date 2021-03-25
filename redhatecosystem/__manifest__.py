# -*- coding: utf-8 -*-
{
    'name': "redhatecosystem",

    'summary': "Piros Red Hat Ecosystem extensions",

    'description': "Piros Red Hat Ecosystem extensions",

    'author': "Piros",
    'website': "https://www.piros.be",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.7',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'purchase', 'sale_margin'],

    # always loaded
    'data': [
        #'views/views.xml',
    ],
}
