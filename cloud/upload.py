import http.client
import os

from datetime import datetime

API_HOST = "rhz3bho1fk.execute-api.ap-southeast-2.amazonaws.com"
API_KEY = os.getenv("API_KEY")

BUCKET_NAME = "2022t3comp6733-smartedgebucket"

def upload_binary(filename, path):
	with open(path, "rb") as f:
		b = f.read()

		conn = http.client.HTTPSConnection(API_HOST)

		headers = { 'X-API-KEY': API_KEY }
		conn.request("PUT", "/v1/%s/%s" % (BUCKET_NAME, filename), b, headers)

		resp = conn.getresponse()
		print(resp.status)

def _upload_json(filename, json_str):
	conn = http.client.HTTPSConnection(API_HOST)

	headers = { 'X-API-KEY': API_KEY }
	conn.request("PUT", "/v1/%s/%s" % (BUCKET_NAME, filename), json_str, headers)

	resp = conn.getresponse()
	print(resp.status)

def upload_trip_meta(trip_name, data_json):
	filename = "%s_%s_meta.json" % (trip_name, datetime.now().strftime("%Y%m%d%H%M%S"))
	_upload_json(filename, data_json)
