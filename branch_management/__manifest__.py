{
    'name': 'Branch Management',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Multi-branch support for Odoo Community',
    'description': """
        This module provides multi-branch support for Odoo Community Edition.
        Features:
        - Branch management
        - Data isolation between branches
        - Branch-specific views and filters
        - Branch dashboard
    """,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'depends': [
        'base',
        'hr',
        'calendar',
        'crm',
    ],
    'data': [
        'security/branch_security.xml',
        'security/ir.model.access.csv',
        'views/hr_employee_views.xml',
        'views/res_partner_views.xml',
        'views/res_users_views.xml',
        'views/calendar_views.xml',
        'views/crm_views.xml',
        'views/branch_views.xml',
        'views/menu_views.xml',
        'data/demo_data.xml',
    ],
    'demo': [
        'data/demo_data.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
} 