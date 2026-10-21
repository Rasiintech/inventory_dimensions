frappe.ui.form.on("Delivery Note Item", {
	shelf: function (frm, cdt, cdn) {
		let row = locals[cdt][cdn];
		if (row.warehouse && row.item_code && row.shelf) {
			frappe.call({
				method: "inventory_dimensions.inventory_dimensions.customizations.delivery_note.delivery_note.get_total_shelf_qty",
				args: {
					item_code: row.item_code,
					warehouse: row.warehouse,
					shelf: row.shelf,
				},
				callback: function (r) {
					console.log(r.message[0].total);
					if (r.message) {
						frappe.model.set_value(cdt, cdn, "custom_shelf_qty", r.message[0].total);
					}
				},
			});
		} else {
			frappe.model.set_value(cdt, cdn, "custom_shelf_qty", 0);
		}
	},
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
frappe.ui.form.on("Delivery Note", {
	refresh: function (frm) {
		rack_filter_query(frm);
		shelf_filter_query(frm);
	},
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
	validate(frm) {
		frm.doc.items.forEach(row => {
			if (row.custom_shelf_qty && row.qty > row.custom_shelf_qty) {
				frappe.throw(`Row ${row.idx}: Qty cannot be greater than Shelf Qty.`);
			}
		});
	},
});

function rack_filter_query(frm) {
	let rack_filter = [];
	frm.set_query("rack", "items", function (doc, cdt, cdn) {
		var d = locals[cdt][cdn];
		if (d.warehouse && d.item_code) {
			frappe.call({
				method: "inventory_dimensions.inventory_dimensions.customizations.delivery_note.delivery_note._get_rack_list",
				async: false,
				args: {
					item_code: d.item_code,
					warehouse: d.warehouse,
				},
				callback(r) {
					rack_filter = r.message;
				},
			});
		}
		return {
			filters: {
				name: ["in", rack_filter],
			},
		};
	});
}

function shelf_filter_query(frm) {
	let shelf_filter = [];
	frm.set_query("shelf", "items", function (doc, cdt, cdn) {
		var d = locals[cdt][cdn];
		if (d.warehouse && d.item_code && d.rack) {
			frappe.call({
				method: "inventory_dimensions.inventory_dimensions.customizations.delivery_note.delivery_note._get_shelf_list",
				async: false,
				args: {
					item_code: d.item_code,
					warehouse: d.warehouse,
					rack: d.rack,
				},
				callback(r) {
					shelf_filter = r.message;
				},
			});
		}
		return {
			filters: {
				name: ["in", shelf_filter],
			},
		};
	});
}
