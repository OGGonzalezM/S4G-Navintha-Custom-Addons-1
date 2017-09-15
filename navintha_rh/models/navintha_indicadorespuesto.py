from openerp import fields, models

class Navintha_indicadorespuesto(models.Model):
    _name = 'hr.job_indicadorespuesto'
    
    name = fields.Char(string="Indicador",help="Nombre del indicador")
