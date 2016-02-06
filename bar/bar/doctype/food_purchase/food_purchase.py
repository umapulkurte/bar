# -*- coding: utf-8 -*-
# Copyright (c) 2015, wayzon and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class FoodPurchase(Document):
	def on_submit(self):
		date=self.date
		ls=self.food_purchase_item
		for i in range(len(ls)):
			material_name=ls[i].material_name
			#item_name = ls[i].item_name
			#item_code = ls[i].item_code
			uom=ls[i].uom
			qnty=ls[i].quantity
			#q1=frappe.db.sql("""select quantity from `tabGodown Stock` where item_name=%s and uom=%s and item_code=%s""",(item_name,uom,item_code))
			#if q1:
			#	query=frappe.db.sql("""update `tabGodown Stock` 
			#	set quantity=quantity+%s 
			#	where item_name=%s and uom=%s and item_code=%s""",(qnty,item_name,uom,item_code))
			#	frappe.msgprint("Godown Stock Updated")
			#else:
			#	q3=frappe.db.sql("""select max(cast(name as int)) from `tabGodown Stock`""")[0][0]
			#	if q3:
			#		name=int(q3)+1;
			#	else:
			#		name=1	
			#	q2=frappe.db.sql("""insert into `tabGodown Stock` set name=%s, item_name=%s, uom=%s, quantity=%s, item_code=%s""",(name,item_name,uom,qnty,item_code))
			#	frappe.msgprint("New Entry addede in Godown Stock!")

	def on_cancel(self):
		ls=self.food_purchase_item
		for i in range(len(ls)):
			material_name=ls[i].material_name
			uom=ls[i].uom
			item_name = ls[i].item_name
			item_code = ls[i].item_code
			qnty=ls[i].quantity
			#q1=frappe.db.sql("""select quantity from `tabGodown Stock` where item_name=%s and uom=%s and item_code=%s """,(item_name,uom,item_code))
			#if q1:
			#	query=frappe.db.sql("""update `tabGodown Stock` 
			#	set quantity=quantity-%s 
			#	where item_name=%s and uom=%s and item_code=%s""",(qnty,item_name,uom,item_code))
			#	frappe.msgprint("Godown Stock Updated")

#@frappe.whitelist()
#def get_item_detail(itm):
#	q=frappe.db.sql("""select item_name,rate,item_code from `tabItems` where name=%s""",itm)
#	return (q)

@frappe.whitelist()
def get_money_in_words(n):
	from frappe.utils import money_in_words
	from frappe.utils import in_words
	x=money_in_words(n)
	return (x)

@frappe.whitelist()
def get_item_detail(itm):
	#q=frappe.db.sql("""select item_name,rate,item_code,uom from `tabItems` where name=%s and item_sub_group='Kitchen Items' and item_group='Purchase Items'""",itm)
	q=frappe.db.sql("""select item_name,rate,item_code,uom from `tabItems` where name=%s and item_sub_group='Kitchen Items'""",itm)
	return (q)