# -*- coding: utf-8 -*-
from openerp import fields, models

class Estudios_capacitaciones(models.Model):
	_name = 'hr.estudios_capacitaciones'

        x_navintha_estudios_name = fields.Char(string="Nombre",
        	help="nombre de la capacitación")

	x_navintha_estudios_descripcion = fields.Text(string="Descripcion",help="Descripción de estudios")

	x_navintha_nivel = fields.Char(string="Nivel",help="Nivel")

	x_navintha_institucion = fields.Char(string="Institución",help="Institución")

	x_navintha_estudios_fechainicio = fields.Date(string="Fecha de inicio",help="Fecha de inicio del estudio")

	x_navintha_estudios_fechafin = fields.Date(string="Fecha fin",help="Fecha fin del estudio")

        x_navintha_estudios_personal = fields.Many2one('res.partner', string="Personal",help="Personal")

