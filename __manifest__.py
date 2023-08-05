# -*- coding: utf-8 -*-
{
    'name': "Coreline BTCO",

    'summary': """
    """,

    'description': """
    """,

    'author': 'Coreline',
    'website': 'https://www.coreline.tech',
    'category': 'Services',
    'version': '16.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['product', 'sale', 'website_sale', 'stock'],

    # always loaded
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'security/record_rules.xml',
        'views/flower_flower.xml',
        'views/product_template.xml',
        'views/sale_order.xml',
        'views/templates.xml',
        'views/stock_lot_view.xml',
        'views/stock_warehouse.xml',
        'data/server_actions.xml',
        'data/paper_format.xml',
        'data/parameters.xml',
        'data/scheduled_actions.xml',
        'reports/sale_order_flowers.xml'
    ],
}
