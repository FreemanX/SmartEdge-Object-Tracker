import http.client
import os

API_HOST = "50pkh1qo9d.execute-api.us-east-1.amazonaws.com"
API_KEY = os.getenv("API_KEY")

LATITUDE = "-16.358376"
LONGITUDE = "145.787559"
BUCKET_NAME = "comp6733s%ss%s" % (LATITUDE, LONGITUDE)

def smartedge_filename(date, simple_filename):
	if date.isdigit() != True or len(date) != 14:
		raise Exception("expect date to be in the format of YYYYMMDDHHIISS")
	return "%s_%s" % (date, simple_filename)

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
