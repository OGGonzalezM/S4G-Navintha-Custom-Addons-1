# -*- coding: utf-8 -*-

from openerp import fields, models

class Navintharh(models.Model):
	_inherit = 'hr.job'

	x_navintha_fechadeelaboracion = fields.Date(string="Fecha de elaboración",help="Fecha de Elaborción")
	x_navintha_fechadeaprovacion = fields.Date(string="Fecha de aprobación",help="Fecha de Aprobación")
	x_navintha_propositodelpuesto = fields.Text(string="Propósito del puesto",help="Propósito del puesto")
    	x_navintha_plantillaminimanecesaria = fields.Integer(string="Plantilla minima necesaria")


	#x_navintha_relacionesinternas_delpuestoconotros = fields.Text(string="Relaciones internas con otros puestos",help="Relaciones internas con otros puestos")
        #x_navintha_responsabilidades = fields.Many2one('res.partner', string="Responsabilidades")
	x_navintha_relacionesexternas = fields.Many2many('navintha.relexternas','name','relacionext',
            string="Relaciones externas con otros puestos",help="Relaciones externas con otros puestos")

	#x_navintha_responsabilidades_descripcion = fields.Text(string="Responsabilidades y frecuencia de realización")

	#x_navintha_responsabilidades_frecuenciaderealizacion = fields.Text(string="Frecuencia de realización")
	x_navintha_responsabilidades = fields.Many2many('navintha.responsabilidades',
	                                                 'name','x_navintha_resfrecuencia', 
		                                             string="Responsabilidades",
		                                             help="Elija o crea la responsabilidad y la frecuencia de su realización")

	x_navintha_ltd_desicion = fields.Boolean(string="Libertad para toma de desiciones",help="Libertad para toma de desiciones")

	x_navintha_condicionesdeltrabajo = fields.Text(string="Condiciones del trabajo",help="Condiciones del trabajo")

	#Perfil del puesto
	x_navintha_edad = fields.Selection(selection=[('20 - 25','20 - 25 Años'),
                                                      ('25 - 30','25 - 30 Años'),
                                                      ('30 - 35','30 - 35 Años'),
                                                      ('35 - 40','35 - 40 Años'),
                                                      ('40 - 45','40 - 45 Años'),
                                                      ('45 - 50','45 - 50 Años'),
                                                      ('50 - 55','50 - 55 Años'),
                                                      ('55 - 60','55 - 60 Años'),
                                                      ('60 - 65','60 - 65 Años'),
                                                      ('65 - 70','65 - 70 Años')],
                                                      string="Rango de edades",help="Seleccione el rango de edades en la que se encuentra")

        x_navintha_escolaridad = fields.Many2one('hr.escolaridad',
        	 string="Escolaridad",
        	 help="Grado máximo de estudios")

        x_navintha_experiencia = fields.Text(string="Experiencia",
        	help="Trabajos previos")
	
	x_navintha_competenciastecnicas = fields.Text(string="Competencias técnicas",help="Especialidad")
	
	x_navintha_manejomaquinariaequipo = fields.Text(string="Manejo de maquinaria y/o equipo",help="Manejos de los equipos")
	
	x_navintha_manejodesoftware = fields.Text(string="Manejo de software",
		help="Habilidades o uso de software, considere Microsoft Word, Power Point y Excel como básicos")

	x_navintha_idiomas = fields.Text(string="Idiomas",
		help="Que idiomas domina el empleado, no cuente español")
	
	x_navintha_disponibilidadviajar = fields.Boolean(string="Disponibilidad para viajar",help="Puede viajar")

	x_navintha_disponibilidadcambioresidencia = fields.Boolean(string="Disponibilidad de cambio de residencia")
	x_navintha_listadocompetencias = fields.Text(string="Listado de competencias",
		 help="Competencias más destacables del empleado, ejemplos: trabajo en equipo, trabajo bajo presión,  comunicaión efectiva.")

	#Perfiles, competencias, habilidades y capacidades requeridas
	x_navintha_per_comp_hab_cap = fields.Text(string="Perfiles, competencias, habilidades y capacidades requeridas",help="Habilidades")

        x_navintha_skills = fields.Many2many('navintha.competencias', string="Competencias necesarias",help="Competencias necesarias")
        #x_navintha_equipoasignado = fields.Many2many('account.asset', string="Equipo asignable")
        x_navintha_indicadorespuesto = fields.Many2many('kpi', string="Indicadores del puesto",help="Indicadores del puesto")
        
        x_navintha_relacionesinternas = fields.Many2many('navintha.relacionesinternas','relacion', string="Relaciones del puesto")
