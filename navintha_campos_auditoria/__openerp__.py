# -*- coding: utf-8 -*-
{
    'name': "Indexol-Auditorias",

    'summary': """
        Modulo de Auditorias""",

    'description': """
        Para agregar campos a el modelo y vista de auditorias
    """,

    'author': "Soluciones4G",
    'website': "http://www.soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mgmtsystem_audit'],

    # always loaded Recurde cargar deacuerdo al orden deseado
    'data': [
        'views/auditoria_fields_view.xml',
    ],
    'installable':True,
    'auto_install':False,
}
