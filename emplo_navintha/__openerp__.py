# -*- coding: utf-8 -*-
{
    'name': "emplo_navintha",

    'summary': """
        aditional requirements to employees
    """,

    'description': """
        New Module to add new fields yo emplyees form
    """,

    'author': "Soluciones4G",
    'website': "http://www.soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'hr',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr'],

    # always loaded
    'data': [
        'view/emplo_view.xml',
        'view/numsegemp_view.xml',
    ],
    'installable':True,
    'auto_install':False,
}
