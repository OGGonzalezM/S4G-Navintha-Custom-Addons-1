# -*- coding: utf-8 -*-
from openerp import fields, models

class Numsegsocial(models.Model):
    _inherit = 'hr.employee'

    x_numeroseguridadsocial = fields.Char(string="Nº de seguridad social",
        help="Número de seguridad social del empleado")
