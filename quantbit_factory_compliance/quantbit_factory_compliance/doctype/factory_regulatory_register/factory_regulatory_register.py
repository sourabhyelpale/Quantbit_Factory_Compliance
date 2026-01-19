# Copyright (c) 2026, Quantbit Technologies and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class FactoryRegulatoryRegister(Document):
    pass
	# def before_save(self):
	# 	due = self.due_day
	# 	if(due < 1 or due  > 31):
	# 		frappe.log_error("Enter date between 1-31")