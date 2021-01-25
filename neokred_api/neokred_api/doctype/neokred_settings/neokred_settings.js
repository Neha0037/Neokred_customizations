// Copyright (c) 2021, openetech and contributors
// For license information, please see license.txt

frappe.ui.form.on('Neokred Settings', {
	refresh: function(frm) {
		frm.add_custom_button(__('Call API'), function() {
        frm.trigger("call_api");}, __("Make"));
    },
    call_api: function(frm) {
        frappe.call({
            method: "neokred_api.custom_method.get_neokred_url",
            args: { api_key: frm.doc.api_key, authorization: frm.doc.authorization, client_hash_id: frm.doc.client_hash_id, base_url: frm.doc.base_url},
            callback: function(r) {
                console.log('url---'+r.message);
                window.open(r.message.details.uatUrl);
            }
        });
	}
});