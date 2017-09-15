# -*- coding: utf-8 -*-
from openerp import fields, models

class Relaciones_Internas(models.Model):
	_name = 'navintha.relacionesinternas'

	name = fields.Many2one('hr.job',string="Puesto relacionado")
	relacion = fields.Text(string="Relación del puesto")