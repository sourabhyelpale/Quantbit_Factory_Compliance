# Copyright (c) 2026, Quantbit Technologies and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class License(Document):
	pass

def on_update(self, method=None):
	if not self.disable:
		return
	else:
		frappe.db.sql("""
		UPDATE tabFactory Regulatory Register
		SET license_status = 'Closed'
		WHERE
		category = 'License'
		AND license = %s
		AND docstatus = 1
		""", (self.name,))
		frappe.db.commit()
