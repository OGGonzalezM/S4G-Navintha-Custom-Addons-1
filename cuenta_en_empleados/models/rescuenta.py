# -*- coding: utf-8 -*-
from openerp import fields, models


class Rescuenta(models.Model):
    _inherit = 'res.partner.bank'

    name = fields.Char(string="Responsable de la cuenta",
                       help="Responsable de la cuenta")
