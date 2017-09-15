# -*- coding: utf-8 -*-
from openerp import fields, models

class Relacion_competencias(models.Model):
	_inherit = 'hr.employee'

	x_navintha_comempleado = fields.Many2many('navintha.competenciasempleado', 
		 string="Competencias del empleado",
		 help="Competencias con las que cuenta el empleado, descripcion y nive")
