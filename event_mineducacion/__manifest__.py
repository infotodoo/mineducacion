# -*- coding: utf-8 -*-
{
    'name': "Event Mineducacion",

    'summary': "Event Mineducacion",

    'author': "Todoo SAS",
    'contributors': ['Pablo Arcos pa@todoo.co'],
    'website': "http://www.todoo.co",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Website',
    'version': '12.1',

    # any module necessary for this one to work correctly
    'depends': ['website_event','account_budget','purchase_requisition'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/event_event_view.xml',
        'views/purchase_requisition_view.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}