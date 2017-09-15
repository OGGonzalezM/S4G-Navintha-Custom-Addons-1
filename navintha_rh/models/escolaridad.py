# -*- coding: utf-8 -*-
from openerp import fields, models

class Escolaridad(models.Model):
    _name = 'hr.escolaridad'

    name = fields.Char(string="Escolaridad", help='Escolaridad del empleado')
