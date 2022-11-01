import http.client
import os

API_HOST = "rhz3bho1fk.execute-api.ap-southeast-2.amazonaws.com"
API_KEY = os.getenv("API_KEY")

BUCKET_NAME = "2022t3comp6733-smartedgebucket"

def smartedge_filename(datetime, simple_filename):
	if datetime.isdigit() != True or len(datetime) != 14:
		raise Exception("expect date to be in the format of YYYYMMDDHHIISS")
	return "%s_%s" % (datetime, simple_filename)

def upload_binary(filename, path):
	with open(path, "rb") as f:
		b = f.read()

		conn = http.client.HTTPSConnection(API_HOST)

		headers = { 'X-API-KEY': API_KEY }
		conn.request("PUT", "/v1/%s/%s" % (BUCKET_NAME, filename), b, headers)

		resp = conn.getresponse()
		print(resp.status)

def upload_json(filename, json_str):
	conn = http.client.HTTPSConnection(API_HOST)

	headers = { 'X-API-KEY': API_KEY }
	conn.request("PUT", "/v1/%s/%s" % (BUCKET_NAME, filename), json_str, headers)

	resp = conn.getresponse()
	print(resp.status)
