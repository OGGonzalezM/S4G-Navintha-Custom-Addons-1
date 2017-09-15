# -*- coding: utf-8 -*-
from openerp import fields, models

class Navintha_competencias(models.Model):
	_name = "navintha.competencias"

	name =  fields.Char(string="Nombre de la competencia",
		 help="Son todas aquellas habilidades y aptitudes que tienen las personas que les permiten desarrollar un trabajo de forma exitosa")

	x_navintha_descripcioncompetencia = fields.Char(string="Descripción corta",
		help="Describa brevemente la competencia necesaria")