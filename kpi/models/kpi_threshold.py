# -*- coding: utf-8 -*-
# Copyright 2012 - Now Savoir-faire Linux <https://www.savoirfairelinux.com/>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models, api, exceptions, _


class KPIThreshold(models.Model):
    """KPI Threshold."""

    _name = "kpi.threshold"
    _description = "KPI Threshold"

    @api.multi
    def _compute_is_valid_threshold(self):
        result = {}
        for obj in self:
            # check if ranges overlap
            # TODO: This code can be done better
            for range1 in obj.range_ids:
                for range2 in obj.range_ids:
                    if (range1.valid and range2.valid and
                            range1.min_value < range2.min_value):
                        result[obj.id] = range1.max_value <= range2.min_value
        return result

    @api.multi
    def _compute_generate_invalid_message(self):
        result = {}
        for obj in self:
            if obj.valid:
                result[obj.id] = ""
            else:
                result[obj.id] = ("Two of your ranges are overlapping. Please "
                                  "make sure your ranges do not overlap.")
        return result

    name = fields.Char('Name', size=50, required=True)
    range_ids = fields.Many2many(
        'kpi.threshold.range',
        'kpi_threshold_range_rel',
        'threshold_id',
        'range_id',
        'Ranges'
    )
    valid = fields.Boolean(string='Valid', required=True,
                           compute="_compute_is_valid_threshold", default=True)
    invalid_message = fields.Char(string='Message', size=100,
                                  compute="_compute_generate_invalid_message")
    kpi_ids = fields.One2many('kpi', 'threshold_id', 'KPIs')
    company_id = fields.Many2one(
        'res.company', 'Company',
        default=lambda self: self.env.user.company_id.id)

    @api.model
    def create(self, data):
        # check if ranges overlap
        # TODO: This code can be done better
        range_obj1 = self.env['kpi.threshold.range']
        range_obj2 = self.env['kpi.threshold.range']
        if data.get('range_ids'):
            for range1 in data['range_ids'][0][2]:
                range_obj1 = range_obj1.browse(range1)
                for range2 in data['range_ids'][0][2]:
                    range_obj2 = range_obj2.browse(range2)
                    if (range_obj1.valid and range_obj2.valid and
                            range_obj1.min_value < range_obj2.min_value):
                        if range_obj1.max_value > range_obj2.min_value:
                            raise exceptions.Warning(
                                _("Two of your ranges are overlapping."),
                                _("Make sure your ranges do not overlap!")
                            )
                    range_obj2 = self.env['kpi.threshold.range']
                range_obj1 = self.env['kpi.threshold.range']
        return super(KPIThreshold, self).create(data)

    @api.multi
    def get_color(self, kpi_value):
        color = '#FFFFFF'
        for obj in self:
            for range_obj in obj.range_ids:
                if (range_obj.min_value <= kpi_value <= range_obj.max_value and
                        range_obj.valid):
                    color = range_obj.color
        return color
