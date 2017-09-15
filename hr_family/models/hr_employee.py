# -*- coding: utf-8 -*-
# Copyright (C) 2011 Michael Telahun Makonnen <mmakonnen@gmail.com>.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    fam_spouse = fields.Char("Name")
    fam_spouse_employer = fields.Char("Employer")
    fam_spouse_tel = fields.Char(string="Telefono",help="Teléfono") 
    #Punto Eliminado
    #Personalizados
    fam_spose_borndate = fields.Date(string="Fecha de nacimiento",help="Fecha de nacimiento")
    fam_spouse_address = fields.Char(string="Dirección", help="Dirección de conyugue")

    fam_children_ids = fields.One2many('hr.employee.children', 'employee_id', "Children")
    fam_father = fields.Char("Father's Name",help="Nombre de tu padre")
    fam_father_date_of_birth = fields.Date("Date of Birth", oldname='fam_father_dob',help="Fecha de nacimiento")
    #Personalizado
    fam_address_father = fields.Char(string="Dirección del padre", help="Dirección del Padre del empleado")
    #Dirección del Padre


    fam_mother = fields.Char("Mother's Name",help="Nombre de tu madre")
    fam_mother_date_of_birth = fields.Date("Date of Birth",help="Fecha de nacimiento", oldname='fam_mother_dob')
    fam_address_mother = fields.Char(string="Dirección de la madre", help="Dirección de la Madre del empleado")
    #Dirección de la Madre

