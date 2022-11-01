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

def meta_filename(trip_name):
	return "%s_%s_meta.json" % (trip_name, datetime.now().strftime("%Y%m%d%H%M%S"))

def filename(trip_name, filename):
	return "%s_%s_%s" % (trip_name, datetime.now().strftime("%Y%m%d%H%M%S"), filename)
