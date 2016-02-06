from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Documents"),
			"icon": "icon-star",
			"items": [
				{
					"type": "doctype",
					"name": "Assign Tables",
					"description": _("Assign tables to waiters.")
				},
				{
					"type": "doctype",
					"name": "Food Purchase",
					"description": _("Purchase Daily Raw Food Material.")
				},
				{
					"type": "doctype",
					"name": "Wine Purchase",
					"description": _("Purchase Wine.")
				},
				{
					"type": "doctype",
					"name": "Items",
					"description": _("Item Master.")
				},
				{
					"type": "doctype",
					"name": "Supplier",
					"description": _("Supplier master.")
				},
				{
					"type": "doctype",
					"name": "Waiter",
					"description": _("Waiter Master")
				},
				{
					"type": "doctype",
					"name": "Table",
					"description": _("Table Master.")
				},
				
				
			]
		},
		{
		"label":_("Standard Reports"),
		"icon": "icon-star",
		"items" : [
				

				#{
				#	"type": "doctype",
				#	"name": "Kitchen Stock",
				#	"description": _("Kitchen Stock.")
				#},
				#{
				#	"type": "doctype",
				#	"name": "Counter Stock",
				#	"description": _("Counter Stock.")
				#},
				#{
				#	"type": "doctype",
				#	"name": "Stock",
				#	"description": _("Stock Table.")
				#},
				{
					"type":"report",
					"name" :"Counter Stock",
					"doctype": "Counter Stock",
					"is_query_report": True,
					"description": _("Counter Stock")
				},
				#{
				#	"type":"report",
				#	"name" :"Kitchen Stock",
				#	"doctype": "Kitchen Stock",
				#	"is_query_report": True,
				#	"description": _("Kitchen Stock")
				#},
				{
					"type":"report",
					"name" :"Wine Purchase",
					"doctype": "Wine Purchase",
					"is_query_report": True,
					"description": _("Wine Purchase Stock")
				},
				{
					"type":"report",
					"name" :"Food Purchase",
					"doctype": "Food Purchase",
					"is_query_report": True,
					"description": _("Food Purchase Stock")
				},
				{
					"type": "doctype",
					"name": "Godown Stock",
					"description": _("Godown Stock.")
				},
		]
	}
	]