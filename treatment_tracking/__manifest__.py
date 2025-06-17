{
    'name': 'Treatment Tracking',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Track treatments and link them to sales orders',
    'description': """
        This module allows tracking of treatments and links them to sales orders.
        Features:
        - Treatment types management
        - Treatment tracking in calendar events
        - Automatic invoice creation
        - Prepaid credit handling
    """,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'depends': [
        'base',
        'sale',
        'calendar',
        'account',
    ],
    'data': [
        'views/treatment_type_views.xml',
        'views/product_views.xml',
        'views/sale_order_views.xml',
        'views/calendar_event_views.xml',
        'views/res_partner_views.xml',
        'views/menu_views.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
} 