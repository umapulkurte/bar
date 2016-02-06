cur_frm.cscript.item_sub_group=function(doc,cdt,cdn)
{
	if (doc.item_sub_group=='Kitchen Items')
	{
		//alert("Select item group correctly");
		cur_frm.set_value('item_group','')
	}
	else
	{
		cur_frm.set_value('item_group','Sale Items')
	}
}