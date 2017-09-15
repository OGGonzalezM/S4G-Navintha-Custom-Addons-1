# -*- coding: utf-8 -*-
from openerp import fields, models

class Skills_empleados(models.Model):
    _inherit = 'hr.employee'

    skill_ids = fields.Many2many('navintha.competencias', string="Competencias del empleado")
