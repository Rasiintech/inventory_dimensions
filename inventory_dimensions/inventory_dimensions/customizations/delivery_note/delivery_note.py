import frappe

from inventory_dimensions.inventory_dimensions.customizations.delivery_note.api_calls.api_call_functions import (
    get_rack_list, get_shelf_list, get_shelf_qty)


## These below 3 functions are call from other files also
@frappe.whitelist()
def get_total_shelf_qty(item_code, warehouse, shelf):
	return get_shelf_qty(item_code, warehouse, shelf)


@frappe.whitelist()
def _get_rack_list(item_code, warehouse):
	return get_rack_list(item_code, warehouse)


@frappe.whitelist()
def _get_shelf_list(item_code, warehouse, rack):
	return get_shelf_list(item_code, warehouse, rack)
