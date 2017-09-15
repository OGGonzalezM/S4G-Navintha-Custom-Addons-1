# -*- coding: utf-8 -*-
{
    'name': "Redireccionado",

    'summary': """
        Redireccion a otro sitio web""",

    'description': """
        Redireccionando el inicio de una sesion en odoo
    """,

    'author': "Soluciones4G",
    'website': "http://www.soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded Recurde cargar deacuerdo al orden deseado
    'data': [
        'views/redireccion_view.xml'
    ],
    'installable':True,
    'auto_install':False,
}
