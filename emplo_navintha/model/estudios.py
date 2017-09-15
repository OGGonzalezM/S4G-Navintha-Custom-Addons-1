#-*- coding:UTF-8 -*-
from openerp import models, fields


class Estudios(models.Model):

    _name = 'estudios.hr'

    name = fields.Char()
    x_fechainicio = fields.Date(string="Fecha de inicio",
                                help="Fecha de inicio")
    x_fechafin = fields.Date(string="Fecha de fin",
                             help="Fecha fin")
    x_descripcion = fields.Text(string="Descripción",
                                help="Descripción de los estudios")
    x_nivel = fields.Char(string="Nivel",
                          help="Nivel")
    x_institucion = fields.Char(string="Institución",
                                help="Institución")
