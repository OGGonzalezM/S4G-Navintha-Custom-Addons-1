from openerp import fields, models

class Empleadosencuestas(models.Model):
	_inherit = 'hr.employee'

	x_navintha_empleadosencuestas = fields.Many2many('survey.survey', string="Encuestas",help="Encuentas")
