{
    'name': 'Custom module for loft Construction',
    'version': '19.0.1.0.0',
    'license': 'LGPL-3',
    'summary': 'Website for loft construction',
    'author': 'Yacine Deradra',
    'depends': ['base', 'website'],
    'data': [
        'security/ir.model.access.csv',
        'views/website_menu.xml',
        'views/home_templates.xml',
        'views/contact_us_template.xml',
        'views/footer_template.xml',
        'views/about_us_template.xml',
        'views/loft_project_views.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'yd_website_loft/static/src/js/loft_project_gallery.js',
            'yd_website_loft/static/src/css/loft_project_card.css',
        ],
    },
    'installable': True,
    'application': True,
}
