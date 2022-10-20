import http.client
import os

API_HOST = "50pkh1qo9d.execute-api.us-east-1.amazonaws.com"
API_KEY = os.getenv("API_KEY")

BUCKET_NAME = "comp6733s-16.358376s145.787559"

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
