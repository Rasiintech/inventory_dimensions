import frappe
from erpnext.stock.doctype.serial_no.serial_no import (
    update_serial_nos_after_submit
)
from erpnext.stock.doctype.stock_entry.stock_entry import StockEntry

from inventory_dimensions.inventory_dimensions.customizations.stock_entry.override.stock_controller import (
    override_update_inventory_dimensions
)


class OverideStockEntry(StockEntry):
	def update_inventory_dimensions(self, row, sl_dict):
		override_update_inventory_dimensions(self, row, sl_dict)

	def on_submit(self):
		self.update_stock_ledger()

		update_serial_nos_after_submit(self, "items")
		self.update_work_order()
		self.validate_subcontract_order()
		self.update_subcontract_order_supplied_items()
		self.update_subcontracting_order_status()
		self.update_pick_list_status()

		self.make_gl_entries()

		self.repost_future_sle_and_gle()
		self.update_cost_in_project()
		self.validate_reserved_serial_no_consumption()
		self.update_transferred_qty()
		self.update_quality_inspection()

		if self.work_order and self.purpose == "Manufacture":
			self.update_so_in_serial_number()

		if self.purpose == "Material Transfer" and self.add_to_transit:
			self.set_material_request_transfer_status("In Transit")
		if self.purpose == "Material Transfer" and self.outgoing_stock_entry:
			self.set_material_request_transfer_status("Completed")

	def on_cancel(self):
		self.update_subcontract_order_supplied_items()
		self.update_subcontracting_order_status()

		if self.work_order and self.purpose == "Material Consumption for Manufacture":
			self.validate_work_order_status()

		self.update_work_order()
		self.update_stock_ledger()

		self.ignore_linked_doctypes = (
			"GL Entry",
			"Stock Ledger Entry",
			"Repost Item Valuation",
		)

		self.make_gl_entries_on_cancel()
		self.repost_future_sle_and_gle()
		self.update_cost_in_project()
		self.update_transferred_qty()
		self.update_quality_inspection()
		self.delete_auto_created_batches()
		self.delete_linked_stock_entry()

		if self.purpose == "Material Transfer" and self.add_to_transit:
			self.set_material_request_transfer_status("Not Started")
		if self.purpose == "Material Transfer" and self.outgoing_stock_entry:
			self.set_material_request_transfer_status("In Transit")
