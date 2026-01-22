# Copyright (c) 2026, Quantbit Technologies and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.naming import make_autoname
from frappe.utils import today



class ComplianceMaster(Document):
	def before_insert(self):
		if not self.compliance_code:
			self.compliance_code = make_autoname(self.series + ".#####")



	# def on_submit(self):
	# 	doc = frappe.get_doc("Factory Regulatory Register",{"name":self.reference_doctype})
	# 	frq = doc.frequency
	# 	period_to = getdate(doc.period_to)

	# 	if frq == "Monthly":
	# 		new_period_to = add_months(period_to,1)

	# 	elif frq == "Quarterly":
	# 		new_period_to = add_months(period_to,3)

	# 	elif frq == "Half-Yearly":
	# 		new_period_to = add_months(period_to,6)

	# 	elif frq == "Annual":
	# 		new_period_to = add_months(period_to,12)

		
	# 	frappe.db.set_value(
	# 		"Factory Regulatory Register",
	# 		doc.name,
	# 		"document",
	# 		self.document
	# 	)

	# 	frappe.db.set_value(
	# 		"Factory Regulatory Register",
	# 		doc.name,
	# 		"period_from",
	# 		doc.period_to
	# 	)

	# 	frappe.db.set_value(
	# 		"Factory Regulatory Register",
	# 		doc.name,
	# 		"period_to",
	# 		new_period_to
	# 	)

	# 	submitted_on = getdate(nowdate())

	# 	if self.due_date > today():
	# 		completion_status = "Completed with Delay"
	# 	else:
	# 		completion_status = "Completed"

	# 	doc.append("task_details", {
	# 		"period_from": self.period_from,
	# 		"period_to": self.period_to,
	# 		"status": completion_status,
	# 		"submitted_on": submitted_on,
	# 	})

	# 	doc.save(ignore_permissions=True)
