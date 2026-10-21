frappe.ui.form.on("Stock Entry Detail", {
	shelf: function (frm, cdt, cdn) {
		let row = locals[cdt][cdn];
		if (row.s_warehouse && row.item_code && row.shelf) {
			frappe.call({
				method: "inventory_dimensions.inventory_dimensions.customizations.delivery_note.delivery_note.get_total_shelf_qty",
				args: {
					item_code: row.item_code,
					warehouse: row.s_warehouse,
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
	s_warehouse: function (frm, cdt, cdn) {
		const row = locals[cdt][cdn];
		if (row.s_warehouse) {
			// Clear Source Rack and Source Shelf fields when Source Warehouse changes
			frappe.model.set_value(cdt, cdn, "rack", null);
			frappe.model.set_value(cdt, cdn, "shelf", null);
		}
	},
	rack: function (frm, cdt, cdn) {
		// Source Rack
		const row = locals[cdt][cdn];
		if (!row.s_warehouse) {
			frappe.throw(__("Please select a Source Warehouse before selecting a Source Rack."));
		} else {
			// Clear Source Shelf when Source Rack changes
			frappe.model.set_value(cdt, cdn, "shelf", null);
		}
	},
	t_warehouse: function (frm, cdt, cdn) {
		const row = locals[cdt][cdn];
		if (row.t_warehouse) {
			// Clear Target Rack and Target Shelf fields when Target Warehouse changes
			frappe.model.set_value(cdt, cdn, "to_rack", null);
			frappe.model.set_value(cdt, cdn, "to_shelf", null);
		}
	},
	to_rack: function (frm, cdt, cdn) {
		// Target Rack
		const row = locals[cdt][cdn];
		if (!row.t_warehouse) {
			frappe.throw(__("Please select a Target Warehouse before selecting a Target Rack."));
		} else {
			// Clear Target Shelf when Target Rack changes
			frappe.model.set_value(cdt, cdn, "to_shelf", null);
		}
	},
});
frappe.ui.form.on("Stock Entry", {
	refresh: function (frm) {
		// rack_filter_query(frm);
		// shelf_filter_query(frm);
	},
	onload: function (frm) {
		// Filter Source Rack field based on Source Warehouse
		frm.fields_dict["items"].grid.get_field("rack").get_query = function (doc, cdt, cdn) {
			const row = locals[cdt][cdn];
			return {
				filters: {
					warehouse: row.s_warehouse, // Filter source racks by the selected source warehouse
				},
			};
		};

		// Filter Source Shelf field based on Source Rack
		frm.fields_dict["items"].grid.get_field("shelf").get_query = function (doc, cdt, cdn) {
			const row = locals[cdt][cdn];
			return {
				filters: {
					rack: row.rack, // Correct field for the selected source rack
				},
			};
		};

		// Filter Target Rack field based on Target Warehouse
		frm.fields_dict["items"].grid.get_field("to_rack").get_query = function (doc, cdt, cdn) {
			const row = locals[cdt][cdn];
			return {
				filters: {
					warehouse: row.t_warehouse, // Filter target racks by the selected target warehouse
				},
			};
		};

		// Filter Target Shelf field based on Target Rack
		frm.fields_dict["items"].grid.get_field("to_shelf").get_query = function (doc, cdt, cdn) {
			const row = locals[cdt][cdn];
			return {
				filters: {
					rack: row.to_rack, // Correct field for the selected target rack
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
		if (d.s_warehouse && d.item_code) {
			frappe.call({
				method: "inventory_dimensions.inventory_dimensions.customizations.delivery_note.delivery_note._get_rack_list",
				async: false,
				args: {
					item_code: d.item_code,
					warehouse: d.s_warehouse,
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
		if (d.s_warehouse && d.item_code && d.rack) {
			frappe.call({
				method: "inventory_dimensions.inventory_dimensions.customizations.delivery_note.delivery_note._get_shelf_list",
				async: false,
				args: {
					item_code: d.item_code,
					warehouse: d.s_warehouse,
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
