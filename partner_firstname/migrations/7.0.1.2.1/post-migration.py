# -*- coding: utf-8 -*-
# Copyright 2017 ABF OSIELL <http://osiell.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


def migrate(cr, version):
    """Check model for proper migration."""
    cr.execute("""
        SELECT count(column_name)
        FROM information_schema.columns
        WHERE table_name = 'res_partner_address'
        AND column_name
        IN ('first_name', 'openupgrade_7_migrated_to_partner_id')
        GROUP BY table_name
        HAVING count(column_name) = 2
        """)
    if cr.fetchall():
        migrate_from_base_partner_surname(cr)


def migrate_from_base_partner_surname(cr):
    """Update res_partner from res_partner_address or former res_partner."""
    cr.execute("""
        UPDATE res_partner rp
        SET firstname=rpa.first_name, lastname=COALESCE(rpa.last_name, rp.name)
        FROM res_partner_address rpa
        WHERE rpa.partner_id = rp.id
        """)
