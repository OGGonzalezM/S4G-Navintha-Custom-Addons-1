# -*- coding: utf-8 -*-
from openerp import models, fields, api

class Navintha_models(models.Model):
    _inherit = 'hr.job'

class Employees(models.Model):
    _inherit = 'hr.employee'

class Employee_training(models.Model):
	_inherit = 'employee.orientation'

class Conocimiento(models.Model):
	_inherit = 'document.page'

class Encuestas(models.Model):
	_inherit = 'survey.survey'

class MgmSystem(models.Model):
	_inherit = 'mgmtsystem_quality'

class Mgmtsystem(models.Model):
	_inherit='mgmtsystem_nonconformity'

class Navintha_Models(models.Model):
	_name = 'navintha.menu'