# -*- coding: utf-8 -*-
{
    'name': "Rm campos de direccion",

    'summary': """
        Remover campos de dirección en el empleado.""",

    'description': """
        Los campos de dirección en el formulario de empleados se dirijian a res.partner,
        en este modulo se elimina esta relacion y se crean nuevos campos.
    """,

    'author': "Soluciones4G",
    'website': "http://www.soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr'],

    # always loaded Recurde cargar deacuerdo al orden deseado
    'data': [
        'views/address_field_view.xml',
        'views/rmbtnarchivar_view.xml',
    ],
    
    'installable':True,
    'auto_install':False,
}
