# -*- coding: utf-8 -*-
{
    'name': "Navintha - Empleados Encuestas",

    'summary': """
        Agregar Encuestas a los empleados""",

    'description': """
        M2m para agregar encuestas a los empleados
    """,

    'author': "Soluciones4G",
    'website': "http://www.soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr'],

    # always loaded
    'data': [
        'views/empleados_encuestas_view.xml',  
    ],
    'installable':True,
    'auto_install':False,
}
