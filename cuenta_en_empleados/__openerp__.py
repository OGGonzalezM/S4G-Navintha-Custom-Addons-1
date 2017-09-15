# -*- coding: utf-8 -*-
{
    'name': "Rm campo titular cuenta",

    'summary': """
        Hacer invisible el campo de responsable de la cuenta en empleados.""",

    'description': """
        En el formulario de empleados, en la pestana de informacion personal este el campo de numero de cuenta bancaria,
        este abre un nuevo formulario para la creacion del numero de cuenta, en este ultimo aparece el campo de responsable
        de la cuenta, el cual debe ser el mismo trabajador pero abre res.partner, por lo tanto se quitara este campo.
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
        'views/rmrespcuenta_empleado_view.xml',
        'views/mod_cuenta_view.xml',
    ],
    
    'installable':True,
    'auto_install':False,
}
