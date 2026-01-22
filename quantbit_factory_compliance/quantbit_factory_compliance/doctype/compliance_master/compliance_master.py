# Copyright (c) 2026, Quantbit Technologies and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.naming import make_autoname



class ComplianceMaster(Document):
	def before_insert(self):
		if not self.compliance_code:
			self.compliance_code = make_autoname(self.series + ".#####")


def on_update(self, method=None):
	if not self.disable:
		return

	frappe.db.sql("""
		UPDATE `tabFactory Regulatory Register`
		SET compliance_status = 'Closed'
		WHERE
			category = 'Compliance'
			AND compliance = %s
			AND docstatus = 1
	""", (self.name,))

	frappe.db.commit()
