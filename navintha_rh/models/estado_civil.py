# -*- coding: utf-8 -*-
from openerp import fields, models

class Estado_civil(models.Model):
	_inherit = 'hr.employee'

	estadocivil = fields.Selection(
		string="Estado civil",help="Estado civil", selection=[('soltero','Soltero(a)'),
		     ('casado','Casado(a)'),
		     ('viudo','Viudo(a)'),
		     ('divorciado','Divorciado(a)'),
		     ('union_libre','Union libre')]
	)
