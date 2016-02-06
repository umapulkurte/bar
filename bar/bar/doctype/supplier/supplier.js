cur_frm.cscript.contact_no=function(doc,cdt,cdn)
{
	var n = doc.contact_no;
	if((n.length)!=10)
	{
		cur_frm.set_value('contact_no','')
		frappe.throw("Enter 10 digit no.");
	}

}