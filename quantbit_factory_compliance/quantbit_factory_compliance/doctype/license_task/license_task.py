# Copyright (c) 2026, Quantbit Technologies and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import today
from frappe.utils import (
    nowdate,
    getdate,
    add_months,
    add_days
)


class LicenseTask(Document):
	def before_submit(self):
		if not self.document:
			frappe.throw("Please upload document")
		else:
			self.status = "Renewed"


	def before_submit(self):
		self.submitted_on = today()


	def on_submit(self):

		doc = frappe.get_doc(
			"Factory Regulatory Register",
			self.referance_doctype
		)

		frq = frappe.db.get_value("License",doc.license,"validity_period_months")

		valid_upto = getdate(doc.valid_upto)
		due_date = getdate(doc.due_date)

		new_valid_upto = add_months(valid_upto, int(frq))

		new_due_date = add_days(
			new_valid_upto,
			-int(doc.alert_before_days)
		)

		doc.document = self.document
		doc.issued_on = doc.valid_upto
		doc.valid_upto = new_valid_upto
		doc.due_date = new_due_date

		doc.append("task_details", {
			"period_from": self.issued_on,
			"period_to": self.valid_upto,
			"status": "Renewed",
			"submitted_on": self.submitted_on,
		})

		doc.save(ignore_permissions=True)