from openerp import fields, models


class Evaluacionesempleados(models.Model):
	_inherit = 'survey.survey'

	x_navintha_empleados_evaluados = fields.Many2many('hr.employee', string="Empleados evaluados",help="Empleado evaluado")
