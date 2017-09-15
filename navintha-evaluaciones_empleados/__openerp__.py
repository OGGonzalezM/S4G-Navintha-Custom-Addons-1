# -*- coding: utf-8 -*-
{
    'name': "Navintha - Encuestas Empleados",

    'summary': """
        Agregar empleados a las evaluaciones""",

    'description': """
        M2m para agregar empleados a las evaluaciones
    """,

    'author': "Soluciones4G",
    'website': "http://www.soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','survey'],

    # always loaded
    'data': [
        'views/evaluaciones_empleados_view.xml',
    ], 
    'installable':True,
    'auto_install':False,
}
