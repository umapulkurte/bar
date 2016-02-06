cur_frm.cscript.select_item = function(doc,cdt,cdn)
{
	var d = locals[cdt][cdn];
	var itm = d.select_item;
	frappe.call({
		method:'bar.bar.doctype.wine_purchase.wine_purchase.get_item_detail',
		args:{itm:itm},
		callback:function(r)
		{
			var doclist=frappe.model.sync(r.message)
			d.item_name = doclist[0][0];
			d.rate = doclist[0][1];
			d.item_code = doclist[0][2];
			refresh_field('wine_purchase_item')
			if (d.rate==parseInt(0))
			{
				alert("Please enter Rate for selected item in Item Matser");
			}
		}
	})
}

cur_frm.cscript.quantity = function (doc,cdt,cdn)
{
	var d = locals[cdt][cdn];
	var qty = d.quantity;
	var rt = d.rate;
	var ttl = (qty*rt);
	d.amount = ttl;
	refresh_field('wine_purchase_item')
}

cur_frm.cscript.total_amount=function(doc,cdt,cdn)
{
	var m=doc.wine_purchase_item;
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
