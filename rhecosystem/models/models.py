# -*- coding: utf-8 -*-

from odoo import tools, models, fields, api, registry, _
from odoo.exceptions import UserError

import re

class EcosystemOverview(models.Model):
    _name = 'rhecosystem.ecosystem.overview'
    _auto = False

    x_partner = fields.Char()
    x_category = fields.Char()

    def init(self):
        print("Connected")
        tools.drop_view_if_exists(self.env.cr, 'rhecosystem_ecosystem_overview')
        self.env.cr.execute("""
            CREATE OR REPLACE VIEW rhecosystem_ecosystem_overview AS (
              SELECT
              row_number() OVER () as id,
              res_partner.commercial_company_name as x_partner,
              res_partner_category.name as x_category
              FROM x_res_partner_res_partner_category_rel
              JOIN res_partner ON x_res_partner_res_partner_category_rel.res_partner_id = res_partner.id
              JOIN res_partner_category ON x_res_partner_res_partner_category_rel.res_partner_category_id = res_partner_category.id
              GROUP BY x_partner, res_partner_category.name
              )""")
