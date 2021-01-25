import frappe
import requests

@frappe.whitelist()
def get_neokred_url(api_key,authorization,client_hash_id,base_url):

	headers = {
		'Client-Hash-Id':client_hash_id,
		'api_key': api_key,	
		'Authorization': authorization
	}

	response = requests.get('https://preprod.bankx.money:9091/api/v1/client/onboarding/webUrl',headers=headers)

	return response