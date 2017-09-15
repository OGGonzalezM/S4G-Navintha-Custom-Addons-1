from openerp import fields, models

class Navintha_equipoasignado(models.Model):
    _name = 'hr.equipoasignado'

    name = fields.Char(string="Equipo asignable",help="Equipo asignado")
