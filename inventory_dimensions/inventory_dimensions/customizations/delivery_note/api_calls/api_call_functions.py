import frappe


def get_shelf_qty(item_code, warehouse, shelf):
	shelf_qty = frappe.get_all(
		"Stock Ledger Entry",
		filters={"item_code": item_code, "warehouse": warehouse, "shelf": shelf},
		fields=["sum(actual_qty) as total"],
	)

	if shelf_qty:
		return shelf_qty


def get_rack_list(item_code, warehouse):
	final_list = []
	rack_qty = frappe.get_all(
		"Stock Ledger Entry",
		filters={"item_code": item_code, "warehouse": warehouse},
		group_by="rack",
		fields=["sum(actual_qty) as total", "rack"],
	)

	for i in rack_qty:
		if i["total"] > 0:
			final_list.append(i["rack"])
	return final_list


def get_shelf_list(item_code, warehouse,rack):
	final_list = []
	shelf_qty = frappe.get_all(
		"Stock Ledger Entry",
		filters={"item_code": item_code, "warehouse": warehouse,"rack":rack},
		group_by="shelf",
		fields=["sum(actual_qty) as total", "shelf"],
	)

	for i in shelf_qty:
		if i["total"] > 0:
			final_list.append(i["shelf"])
	return final_list
