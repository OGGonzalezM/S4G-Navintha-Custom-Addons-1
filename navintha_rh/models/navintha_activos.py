# -*- coding: utf-8 -*-
from openerp import fields, models

class Navintha_activos(models.Model):
    _inherit = 'hr.job'

    x_posibleequipo_navintha = fields.Many2many('hr.equipoasignado', 
    	 string="Equipo asignable", 
    	 help='Equipo asignable para un puesto')

