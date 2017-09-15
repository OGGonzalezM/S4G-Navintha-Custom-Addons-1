# -*- coding: utf-8 -*-
{
    'name': "Pruebas - Datos y menú",

    'summary': """
        Datos de la compañia""",

    'description': """
        Modulo para guardar los datos de la compañia y elaborar el menú
    """,

    'author': "Soluciones4G",
    'website': "http://www.soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
     'base',
     'account_asset',
     'account_budget',
     'document',
     'employee_orientation',
     'hr',
     #'hr_skill',
     'hr_holidays',
     'hr_recruitment',
     'hr_equipment',
     'knowledge',
     'mgmtsystem',
     'mgmtsystem_action',
     'mgmtsystem_audit',
     'mgmtsystem_claim',
     'mgmtsystem_nonconformity',
     'mgmtsystem_quality',
     'mgmtsystem_review',
     'mgmtsystem_hazard',
     'navintha_campos_auditoria',
     'emplo_navintha',
     #'navintha-empleados_evaluaciones',
     #'navintha-evaluaciones_empleados',
     'navintha_rh',
     'org_chart_dept',
     'openacademy',
     'purchase',
     #'v9c_backend_theme',
     'survey',
     ],

    # always loaded Recurde cargar deacuerdo al orden deseado
    'data': [
        'views/navintha_profile_view.xml',
        'views/navintha_rh_items_actions.xml',
        'views/navintha_qms_actions_items.xml',
        'views/navintha_rm_actions_items.xml',
        'views/navintha_rfinancieros_actions_items.xml',
        'views/navintha_proveedores_actions_items.xml',
    ],
    'installable':True,
    'auto_install':False,
}
