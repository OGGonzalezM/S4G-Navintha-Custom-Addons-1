# -*- coding: utf-8 -*-
from openerp import fields, models

class Navintha_competencias(models.Model):
	_name = 'navintha.competenciasempleado'

	name =  fields.Char(string="Nombre de la competencia",
		 help="Son todas aquellas habilidades y aptitudes que tienen las personas que les permiten desarrollar un trabajo de forma exitosa")

	x_navintha_descripcion = fields.Char(string="Descripción corta",
		help="Describa brevemente la competencia necesaria")

	x_navintha_nivelcompetencia = fields.Selection(
		 selection=[('excelente','Alto'),
		            ('bueno','Medio'),
		            ('regular','Bajo')],
		            string="Nivel de la competencia",
		            help="Nivel el que se encuentra el trabajador en cuanto a la competencia")