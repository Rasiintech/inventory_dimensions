frappe.ui.form.on('Stock Reconciliation', {
	refresh(frm) {
		// rack_filter_query(frm);
		// shelf_filter_query(frm);
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
})

// frappe.ui.form.on('Stock Reconciliation Item', {
// 	refresh(frm) {
// 		// your code here
// 	},
// })

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