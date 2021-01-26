from __future__ import unicode_literals
import frappe
from frappe import _
import re
import requests, json
from requests.exceptions import HTTPError 

@frappe.whitelist()
def get_neo_activate_card(email,password,api_key,client_hash_id,base_url):
	def get_neokred_token():
		headers = {
			'content-type':'application/json'
		}
		body = {
			'email': email,
			'password': password
		}
		try:
			response = requests.post('https://preprod.bankx.money:9091/api/v1/authenticate',headers=headers,data=json.dumps(body))
			token = response.json()['token']
			return token
		except HTTPError as http_err:
			frappe.throw(_("HTTP Error {0}".format(http_err)))

	neo_kred_token = 'Bearer ' + get_neokred_token()
	headers = {
		'api-key': api_key, 
		'Authorization':  neo_kred_token
		}
	try:
		response = requests.get('https://preprod.bankx.money:9091/api/v1/client/onboarding/webUrl',headers=headers)
		return response.json()['details']['uatUrl']
	except HTTPError as http_err:
		frappe.throw(_("HTTP Error {0}".format(http_err)))