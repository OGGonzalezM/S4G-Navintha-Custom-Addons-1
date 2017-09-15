# -*- coding: utf-8 -*-
##############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#    Copyright (C) 2017-TODAY Cybrosys Technologies(<http://www.cybrosys.com>).
#    Author: Nilmar Shereef(<http://www.cybrosys.com>)
#    you can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    GENERAL PUBLIC LICENSE (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp import models, fields, _


class OrientationChecklist(models.Model):
    _name = 'orientation.checklist'
    _description = "Checklist"
    _rec_name = 'checklist_name'
    _inherit = ['mail.thread', 'ir.needaction_mixin']

    checklist_name = fields.Char(string='Name',help="Nombre", required=True)
    checklist_department = fields.Many2one('hr.department', string='Department',help="Departamento", required=True)
    active = fields.Boolean(string='Active', default=True,
                            help="Establezca active a false para ocultar la lista de verificación de orientación sin eliminarla")
    checklist_line_id = fields.One2many('orientation.check', 'checklist', String="Checklist",help="Checar Lista")


class OrientationChecklistNew(models.Model):
    _name = 'orientation.check'

    checklist_line_name = fields.Many2one('checklist.line', string='Name',help="Nombre")
    checklist_line_user = fields.Many2one('res.users', string='Responsible User',help="Usuario responsable",
                                          related='checklist_line_name.responsible_user')
    expected_date = fields.Date(string="Expected Date",help="Fecha de expedición", default=fields.Datetime.now)
    status = fields.Char(string='Status',help="Estado", readonly=True, default=lambda self: _('New'))
    checklist = fields.Many2one('orientation.checklist', string="Checklist",help="Checar lista", ondelete='cascade')
    relative_field = fields.Many2one('employee.orientation')




