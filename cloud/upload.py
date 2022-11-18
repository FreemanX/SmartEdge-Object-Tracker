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

def zip_filename(filename):
	if filename.endswith(".zip") != True:
		filename += ".zip"
	return "zip_%s" % (filename)

def meta_filename(trip_name, latitude, longitude):
	return "meta_%s_%s_%s_%s.json" % (trip_name, datetime.now().strftime("%Y%m%d%H%M%S"), latitude, longitude)

def filename(trip_name, filename):
	return "%s_%s_%s" % (trip_name, datetime.now().strftime("%Y%m%d%H%M%S"), filename)

import boto3
from botocore.exceptions import ClientError, NoCredentialsError

def upload_s3(filepath, object_name):
	# S3_KEY_ID = os.getenv("S3_KEY_ID")
	# S3_SECRET_KEY = os.getenv("S3_SECRET_KEY")

	S3_KEY_ID = '123'
	S3_SECRET_KEY = '345'
	
	s3_client = boto3.client(
		"s3",
		aws_access_key_id=S3_KEY_ID,
		aws_secret_access_key=S3_SECRET_KEY,
	)

	with open(filepath, "rb") as f:
		try:
			s3_client.upload_fileobj(f, BUCKET_NAME, object_name)

		except ClientError as err:
			raise Exception(err.response['Error']['Message'])
		except NoCredentialsError as err:
			raise Exception(err.response['Error']['Message'])
