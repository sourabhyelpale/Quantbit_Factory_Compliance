# Copyright (c) 2026, Quantbit Technologies and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import getdate, today, add_days
from frappe.utils import nowdate
from datetime import date
import calendar


class FactoryRegulatoryRegister(Document):


    def before_save(self):

        if self.category == "Compliance":
            if not self.referance_no:
                frappe.throw("Please Enter Reference Number")
            if self.period_to:
                self.due_date = add_days(
                    self.period_to,
                    -int(self.alert_before_days)
                )


        elif self.category == "License":
            if self.valid_upto:
                self.due_date = add_days(
                    self.valid_upto,
                    -int(self.alert_before_days)
                )



