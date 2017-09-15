# -*- coding: utf-8 -*-
{
    'name': "Remover campos",

    'summary': """
        Remover campos que no se notaron muy utiles""",

    'description': """
        Campos que no se hicieron muy utiles, remover u ocultarlos
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
        'views/remove_tagsincontact_view.xml',
        'views/remove_notebookincontacts_view.xml',
        #'views/test.xml',
    ],
    'installable':True,
    'auto_install':False,
}
