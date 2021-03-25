# -*- coding: utf-8 -*-

from odoo import tools, models, fields, api, registry, _
from odoo.exceptions import UserError

import re

class EcosystemOverview(models.Model):
    _name = 'redhatecosystem.ecosystem.overview'
    _auto = False

    x_partner = fields.Char('Partner')

    def init(self):
        print("Connected")
        tools.drop_view_if_exists(self.env.cr, 'redhatecosystem_ecosystem_overview')
        self.env.cr.execute("""
            CREATE OR REPLACE VIEW redhatecosystem_ecosystem_overview AS (
              SELECT
              row_number() OVER as id,
              res_partner_id,
              res_partner_category_id
              FROM x_res_partner_res_partner_category_rel
              GROUP BY x_res_partner_res_partner_category_rel.res_partner_id
              )""")
