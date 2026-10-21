frappe.ui.form.on("Purchase Receipt Item", {
	warehouse: function (frm, cdt, cdn) {
		const row = locals[cdt][cdn];
		if (row.warehouse) {
			// Clear Rack and Shelf fields when Warehouse changes
			frappe.model.set_value(cdt, cdn, "rack", null);
			frappe.model.set_value(cdt, cdn, "shelf", null);
		}
	},
	rack: function (frm, cdt, cdn) {
		const row = locals[cdt][cdn];
		if (!row.warehouse) {
			frappe.throw(__("Please select a Warehouse before selecting a Rack."));
		} else {
			// Clear Shelf when Rack changes
			frappe.model.set_value(cdt, cdn, "shelf", null);
		}
	},
});

// Apply filters dynamically for Rack and Shelf fields
frappe.ui.form.on("Purchase Receipt", {
	onload: function (frm) {
		// Filter Rack field based on selected Warehouse
		frm.fields_dict["items"].grid.get_field("rack").get_query = function (doc, cdt, cdn) {
			const row = locals[cdt][cdn];
			return {
				filters: {
					warehouse: row.warehouse, // Filter racks by the selected warehouse
				},
			};
		};

		// Filter Shelf field based on selected Rack
		frm.fields_dict["items"].grid.get_field("shelf").get_query = function (doc, cdt, cdn) {
			const row = locals[cdt][cdn];
			return {
				filters: {
					rack: row.rack, // Filter shelves by the selected rack
				},
			};
		};
	},
});
