// Copyright (c) 2024, 8848 Digital LLP and contributors
// For license information, please see license.txt

frappe.ui.form.on('Shelf', {
	warehouse: function (frm){
        if(frm.doc.warehouse){
            frm.set_query('rack', function () {
                return {
                    filters: {
                        warehouse: frm.doc.warehouse // Only show racks linked to the selected warehouse
                    }
                };
            });
        }
        else{
            frm.set_query('rack', function () {
                return {
                    filters: {
                        name: ["in",[]]
                    }
                };
            });

        }
       
    },
});
