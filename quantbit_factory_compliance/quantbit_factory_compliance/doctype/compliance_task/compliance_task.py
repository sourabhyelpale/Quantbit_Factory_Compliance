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



class ComplianceTask(Document):
	def before_submit(self):
		if not self.document:
			frappe.throw("Please upload document")
		else:
			self.status = "Completed"
			self.submitted_on = today()
		

	def on_submit(self):
		doc = frappe.get_doc(
			"Factory Regulatory Register",
			self.reference_doctype
		)

		frq = doc.frequency
		period_to = getdate(doc.period_to)
		due_date = getdate(doc.due_date)

		if frq == "Monthly":
			new_period_to = add_months(period_to, 1)
		elif frq == "Quarterly":
			new_period_to = add_months(period_to, 3)
		elif frq == "Half-Yearly":
			new_period_to = add_months(period_to, 6)
		elif frq == "Annual":
			new_period_to = add_months(period_to, 12)
		else:
			return

		new_due_date = add_days(
			new_period_to,
			-int(doc.alert_before_days)
		)

		# doc.document = self.document
		doc.period_from = doc.period_to
		doc.period_to = new_period_to
		doc.due_date = new_due_date

		if self.due_date and getdate(today()) > getdate(self.due_date):
			completion_status = "Completed with Delay"
		else:
			completion_status = "Completed"

		doc.append("task_details", {
			"period_from": self.period_from,
			"period_to": self.period_to,
			"status": completion_status,
			"submitted_on": self.submitted_on,
		})

		doc.save(ignore_permissions=True)