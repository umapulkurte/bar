cur_frm.cscript.rate = function (doc,cdt,cdn)
{
	var d = locals[cdt][cdn];
	var qty = d.quantity;
	var rt = d.rate;
	var ttl = (qty*rt);
	d.amount = ttl;
	refresh_field('food_purchase_item')
}

cur_frm.cscript.total_amount=function(doc,cdt,cdn)
{
	var m=doc.food_purchase_item;
	var len=m.length;
	var amt=0;
	for(i=0;i<len;i++)
	{
		amt=amt+m[i].amount;
	}
	cur_frm.set_value('total',amt);
	frappe.call({
		method:'bar.bar.doctype.food_purchase.food_purchase.get_money_in_words',
		args:{n:amt},
		callback:function(r)
		{
			cur_frm.set_value('amount_in_words',r.message)
		}
	})
}

/*cur_frm.fields_dict["food_purchase_item"].grid.get_field("material_name").get_query = function(doc,cdt,cdn) {
	var child=locals[cdt][cdn];
	var item1=child.item_code;
	return {
		filters: {
			'item_name': item1,
			//'item_group':'Purchase Items',
			'item_sub_group':'Kitchen Items'
		}
	}
}

cur_frm.cscript.material_name=function(doc,cdt,cdn)
{
	var d = locals[cdt][cdn];
	var itm = d.material_name;
	frappe.call({
		method:'bar.bar.doctype.food_purchase.food_purchase.get_item_detail',
		args:{itm:itm},
		callback:function(r)
		{
			var doclist=frappe.model.sync(r.message)
			d.item_name = doclist[0][0];
			d.item_code = doclist[0][2];
			d.uom = doclist[0][3]
			refresh_field('food_purchase_item')
		}
	})
}*/