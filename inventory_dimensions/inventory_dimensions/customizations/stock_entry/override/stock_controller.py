import frappe
from erpnext.stock.doctype.inventory_dimension.inventory_dimension import (
    get_evaluated_inventory_dimension
)


def override_update_inventory_dimensions(self, row, sl_dict) -> None:
	# To handle delivery note and sales invoice
	if row.get("item_row"):
		row = row.get("item_row")

	dimensions = get_evaluated_inventory_dimension(row, sl_dict, parent_doc=self)
	for dimension in dimensions:
		if not dimension:
			continue

		if self.doctype in [
			"Purchase Invoice",
			"Purchase Receipt",
			"Sales Invoice",
			"Delivery Note",
			"Stock Entry",
		]:
			if (
				(
					sl_dict.actual_qty > 0
					and not self.get("is_return")
					or sl_dict.actual_qty < 0
					and self.get("is_return")
				)
				and self.doctype in ["Purchase Invoice", "Purchase Receipt"]
			) or (
				(
					sl_dict.actual_qty < 0
					and not self.get("is_return")
					or sl_dict.actual_qty > 0
					and self.get("is_return")
				)
				and self.doctype in ["Sales Invoice", "Delivery Note", "Stock Entry"]
			):
				sl_dict[dimension.target_fieldname] = row.get(dimension.source_fieldname)
			else:
				fieldname_start_with = "to"
				if self.doctype in ["Purchase Invoice", "Purchase Receipt"]:
					fieldname_start_with = "from"

				fieldname = f"{fieldname_start_with}_{dimension.source_fieldname}"
				sl_dict[dimension.target_fieldname] = row.get(fieldname)

				if (
					not sl_dict.get(dimension.target_fieldname) and not self.doctype == "Stock Entry"
				):
					sl_dict[dimension.target_fieldname] = row.get(dimension.source_fieldname)

				if not sl_dict.get(dimension.target_fieldname) and self.doctype == "Stock Entry":
					sl_dict[dimension.target_fieldname] = None

		elif row.get(dimension.source_fieldname):
			sl_dict[dimension.target_fieldname] = row.get(dimension.source_fieldname)

		if not sl_dict.get(dimension.target_fieldname) and dimension.fetch_from_parent:
			sl_dict[dimension.target_fieldname] = self.get(dimension.fetch_from_parent)

			# Get value based on doctype name
			if not sl_dict.get(dimension.target_fieldname):
				fieldname = next(
					(
						field.fieldname
						for field in frappe.get_meta(self.doctype).fields
						if field.options == dimension.fetch_from_parent
					),
					None,
				)

				if fieldname and self.get(fieldname):
					sl_dict[dimension.target_fieldname] = self.get(fieldname)

			if sl_dict[dimension.target_fieldname] and self.docstatus == 1:
				row.db_set(dimension.source_fieldname, sl_dict[dimension.target_fieldname])
