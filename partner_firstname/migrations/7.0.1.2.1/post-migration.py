# -*- coding: utf-8 -*-
# Copyright 2017 ABF OSIELL <http://osiell.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


def migrate(cr, version):
    cr.execute("""
        SELECT column_name
        FROM information_schema.columns
        WHERE table_name = 'res_partner_address'
        AND column_name = 'first_name'
        """)
    if cr.fetchall():
        migrate_from_base_partner_surname(cr)


def migrate_from_base_partner_surname(cr):
    cr.execute("""
        UPDATE res_partner
        SET firstname = rpa.first_name, lastname = rpa.last_name
        FROM res_partner_address rpa
        WHERE rpa.openupgrade_7_migrated_to_partner_id = res_partner.id
        """)