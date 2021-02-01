// Copyright (c) 2021, openetech and contributors
// For license information, please see license.txt

frappe.ui.form.on('Neokred Settings', {
	refresh: function(frm) {
		frm.add_custom_button(__('Call API'), function() {
        frm.trigger("call_api");}, __("Make"));
        frm.add_custom_button(__('Check Status'), function() {
        frm.trigger("check_status");}, __("Make"));
    },
    call_api: function(frm) {
        frappe.call({
            method: "neokred_api.custom_method.get_neo_activate_card",
            args: { email: frm.doc.email, password: frm.doc.password, api_key: frm.doc.api_key, client_hash_id: frm.doc.client_hash_id, base_url: frm.doc.base_url},
            callback: function(r) {
                window.open(r.message);
            }
        });
	},
	check_status: function(frm) {
        frappe.call({
            method: "neokred_api.custom_method.get_neo_check_card_status",
            args: { email: frm.doc.email, password: frm.doc.password, api_key: frm.doc.api_key, client_hash_id: frm.doc.client_hash_id, base_url: frm.doc.base_url, mobile_number: frm.doc.mobile_number},
            callback: function(r) {
            	console.log(r.message.details);
            }
        });
	}
});