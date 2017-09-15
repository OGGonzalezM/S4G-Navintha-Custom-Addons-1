# -*- coding: utf-8 -*-
from dateutil.relativedelta import relativedelta
from datetime import timedelta
from openerp import api, fields, models


class emplo_navintha(models.Model):

    _inherit = 'hr.employee'

    x_numempleado = fields.Char(string="Número de empleado",
                                help="Número de control del empleado")

    x_contratacion = fields.Datetime(string="Fecha de contratación",
                                     help="Fecha de contratación")

    x_antiguedad = fields.Char(string="Antigüedad",
                               help="Antigûedad",
                               readonly=True,
                               compute='_total_minutes')
    x_fechaactual = fields.Datetime(default=fields.Datetime.now)

    x_observaciones = fields.Text(string="Observaciones",
                                  help="Observaciones en el empleado")

    #x_fechaactual = fields.Datetime(default=fields.Datetime.today())
    #x_fechaactual = fields.Datetime(default=fields.Datetime.now)

    x_perfilacademico = fields.Many2one('hr.escolaridad',
                                        string="Perfil académico",
                                        help="")

    # Campos para los documentos
    x_navintha_documentos_actanacimiento = fields.Boolean(string="Acta de nacimiento",
                                                          help="Si el empleado presentó este documento marque la casilla")

    # x_navintha_documentos **********************
    x_navintha_documentos_contrato = fields.Boolean(string="Contrato laboral",
      help="El empleado tiene contrato laboral")
    
    x_navintha_documentos_contratoconfidencial = fields.Boolean(string="Contrato de confidencialidad",
      help="El empleado tiene contrato de confidencialidad")
    
    x_navintha_documentos_cedulaprofesional = fields.Boolean(string="Cédula profesional",
      help="Si el empleado tiene cedula profesional marque la casilla")
    
    x_navintha_documentos_rfc = fields.Boolean(string="RFC",
      help="El empleado tiene RFC")
    
    x_navintha_documentos_cartasrecomendacion = fields.Boolean(string="Cartas de recomendación",
      help="Si el empleado presenta cartas de recomendación marque la casilla")
    
    x_navintha_documentos_evaluacion = fields.Boolean(string="Evaluación",
      help="Si al empleado se le ha evaluado marque la casilla")
    
    #Documentos base
    x_navintha_documentos_ine = fields.Boolean(string="INE",
                                               help="Si el empleado presentó este documento marque la casilla")

    x_navintha_documentos_comprobantedomicilio = fields.Boolean(string="Comprobante de domicilio",
                                                                help="Si el empleado presentó este documento marque la casilla")

    x_navintha_documentos_curp = fields.Boolean(string="CURP",
                                                help="Si el empleado presentó este documento marque la casilla")

    x_navintha_documentos_cv = fields.Boolean(string="Currículum Vitae",
                                              help="Si el empleado presentó este documento marque la casilla")

    x_navintha_documentos_comprobanteestudios = fields.Boolean(string="Comprobante de estudios",
                                                               help="Si el empleado presentó este documento marque la casilla")

    @api.one
    @api.depends('x_contratacion', 'x_fechaactual')
    def _total_minutes(self):
        if self.x_contratacion and self.x_fechaactual:
            start_dt = fields.Datetime.from_string(self.x_contratacion)
            finish_dt = fields.Datetime.from_string(self.x_fechaactual)
            difference = relativedelta(finish_dt, start_dt)
            year = difference.years
            month = difference.months
            days = difference.days
            self.x_antiguedad = str(year) + " años " + \
                str(month) + " meses " + str(days) + " dias"
        return {}
