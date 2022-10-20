import boto3
import logging
import os

from botocore.exceptions import ClientError
from fastapi import FastAPI, Response
from typing import Union

S3_KEY_ID = os.getenv("S3_KEY_ID")
S3_SECRET_KEY = os.getenv("S3_SECRET_KEY")

app = FastAPI()
logger = logging.getLogger(__name__)

s3_client = boto3.client(
	"s3",
	aws_access_key_id=S3_KEY_ID,
	aws_secret_access_key=S3_SECRET_KEY,
)
s3_resource = boto3.resource(
	"s3",
	aws_access_key_id=S3_KEY_ID,
	aws_secret_access_key=S3_SECRET_KEY,
)

BUCKET_PREFIX = "comp6733"

def bucket_name_from_location(location):
	location = location.replace("_", "s")
	return "%ss%s" % (BUCKET_PREFIX, location)

@app.get("/health")
async def health_check():
    return {"status": "OK"}

@app.get("/locations")
async def list_locations():
	try:
		buckets_resp = s3_client.list_buckets()
	except ClientError:
		logger.exception("Couldn't list buckets.")
		raise

	resp = {"locations": []}
	for bucket in buckets_resp["Buckets"]:
		name_parts = bucket["Name"].split("s")
		if name_parts[0] == BUCKET_PREFIX:
			resp["locations"].append("%s_%s" % (name_parts[1], name_parts[2]))

	return resp

@app.get("/{location}/data")
def list_data(location, date: Union[str, None] = None):
	bucket_name = bucket_name_from_location(location)
	try:
		s3_bucket = s3_resource.Bucket(bucket_name)
		objects = None
		if date:
			objects = s3_bucket.objects.filter(Prefix=date)
		else:
			objects = s3_bucket.objects.all()
	except ClientError:
		logger.exception("Couldn't list objects in bucket %s." % (bucket_name))

	resp = {"data": []}
	for object in objects:
		resp["data"].append(object.key)
	
	return resp

@app.get("/{location}/data/{key}")
def get_object(location, key):
	bucket_name = bucket_name_from_location(location)
	try:
		s3_bucket = s3_resource.Bucket(bucket_name)
		s3_object = s3_bucket.Object(key)

		body = s3_object.get()['Body'].read()
		response = Response(content=body)
		return response
	except ClientError:
		logger.exception(
			"Couldn't get object '%s' from bucket '%s'.",
			s3_object.key,
			s3_bucket.name,
		)
		raise
