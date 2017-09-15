# -*- coding: utf-8 -*-
from openerp import fields, models

class Relacionesexternas(models.Model):
    _name = 'navintha.relexternas'

    name = fields.Char(string="Nombre del puesto",
        help="Nombre del puesto relacionado")

    relacionext = fields.Char(string="Relación del puesto",
        help="Relación externa del puesto")
