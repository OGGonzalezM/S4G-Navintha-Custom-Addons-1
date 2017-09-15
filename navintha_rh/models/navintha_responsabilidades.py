# -*- coding: utf-8 -*-
from openerp import fields, models

class Navintha_responsabilidades(models.Model):
	_name = "navintha.responsabilidades"

	name = fields.Char(string="Nombre de la responsabilidad",
		help="Nombre de la responsabilidad")

	x_navintha_respdescripcion = fields.Text(string="Describa brevemente la responsabilidad",
		help="Describa brevemente la responsabilidad")
	x_navintha_resfrecuencia = fields.Selection(selection=[('diaria','Realizar a diario'),
		                                                	 ('semanal','Semanalmente'),
		                                                	 ('quincenal','Cada dos semanas'),
		                                                	 ('mensual','Mensualmente'),
		                                                	 ('dosmeses','Cada dos meses'),
		                                                	 ('trimestral','Trimestral'),
												             ('semestral','Semestral'),
												             ('anual','Anual')],
		                                                	help="Seleccione cada que tiempo se deberá realizar la tarea",
		                                                	string="Frecuencia de realización")