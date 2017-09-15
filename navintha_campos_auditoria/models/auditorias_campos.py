# -*- coding: utf-8 -*-
from openerp import fields, models

class Auditorias_campos(models.Model):
	_inherit = 'mgmtsystem.audit'

	x_indexol_auditoriafin = fields.Date(string="Fecha fin",help="")
	x_indexol_tipoauditoria = fields.Selection(string="Tipo de auditoría",help="Selecciona el tipo de auditoría", selection=[('Interna', 'Interna'),('Externa','Externa')])
	x_indexol_confirmarasistencia = fields.Boolean(string="Confirmar asistencia")