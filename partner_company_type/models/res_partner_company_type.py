# -*- coding: utf-8 -*-
# Copyright 2017 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ResPartnerCompanyType(models.Model):

    _name = 'res.partner.company.type'
    _description = 'Partner Company Type'

    name = fields.Char(string='Title', required=True, translate=True)
    shortcut = fields.Char(string='Abbreviation', translate=True)

    _sql_constraints = [('name_uniq', 'unique (name)',
                         "Partner Company Type already exists!")]

    @api.multi
    def name_get(self):
        res = []
        for type_ in self:
            shortcut = type_.shortcut and '(' + type_.shortcut + ') ' or ''
            res.append((type_.id, shortcut + type_.name))
        return res
