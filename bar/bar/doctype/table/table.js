cur_frm.cscript.table_no=function(doc,cdt,cdn)
{
	var t = doc.table_no;
	frappe.call({
		method:'bar.bar.doctype.table.table.check_tableno',
		args:{t:t},
		callback:function(r)
		{
			if (r.message==1)
			{
				cur_frm.set_value('table_no','');
			}
		}
	})
}