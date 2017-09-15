# -*- coding: utf-8 -*-
from openerp import fields, models

class Navintha_employee_directory(models.Model):
	_inherit = 'res.partner'

	x_navintha_perfilacademico = fields.Char(string="Perfil academico",
		help="Grado de estudios")

	x_navintha_empleadoobservaciones = fields.Text(string="Observaciones",
		help="Observaciones o puntos a destacar")

	x_navintha_estudios = fields.One2many('hr.estudios_capacitaciones',
		 'x_navintha_estudios_name',
		  string="Estudios y capacitaciones",help="Estudios y Capacitaciones")

