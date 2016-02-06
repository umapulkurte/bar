# -*- coding: utf-8 -*-
# Copyright (c) 2015, wayzon and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Table(Document):
	pass

@frappe.whitelist()
def check_tableno(t):
	q= frappe.db.sql("""select name from `tabTable` where table_no=%s""",(t))
	if q:
		frappe.msgprint("Entered table no.already exists")
		return 1
	else:
		return 2