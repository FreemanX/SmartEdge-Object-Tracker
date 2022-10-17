import http.client
import os

API_HOST = "50pkh1qo9d.execute-api.us-east-1.amazonaws.com"
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

def upload_json(filename, json_str):
	conn = http.client.HTTPSConnection(API_HOST)

	headers = { 'X-API-KEY': API_KEY }
	conn.request("PUT", "/v1/%s/%s" % (BUCKET_NAME, filename), json_str, headers)

	resp = conn.getresponse()
	print(resp.status)


upload_binary("test_image1.jpg", "/Users/yinlokwong/Desktop/310691998_443816850955288_4729957535753765889_n.png")
payload = '{"test-field1": "test-data1", "test-field2": "test-data2"}'
upload_json("test_json1.json", payload)
