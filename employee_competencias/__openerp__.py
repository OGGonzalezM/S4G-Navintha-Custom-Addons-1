# -*- coding: utf-8 -*-
{
    'name': "Competencias de los empleados",

    'summary': """
        Competencias de los empleados""",

    'description': """
       Competencias con las cuales cuenta el empleado, descripcion y nivel
    """,

    'author': "Soluciones4G",
    'website': "http://www.soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr'],

    # always loaded
    'data': [
        'views/competencias_empleado_view.xml',
    ],
    'installable':True,
    'auto_install':False,
}
