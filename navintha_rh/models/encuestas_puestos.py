# -*- coding: utf-8 -*-
from openerp import fields, models

class Encuestas_puestos(models.Model):
	_inherit = 'hr.job'

	x_navintha_encuestas_puestos = fields.Many2many('survey.survey')