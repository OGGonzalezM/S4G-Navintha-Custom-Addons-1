# -*- coding: utf-8 -*-
from openerp import api, fields, models

class Inpartner(models.Model):
	_inherit = "res.partner"

	nuievo = field.Char(string="tested")