import boto3
import logging
import os

from botocore.exceptions import ClientError, NoCredentialsError
from fastapi import FastAPI, Response
from fastapi.responses import StreamingResponse

S3_KEY_ID = os.getenv("S3_KEY_ID")
S3_SECRET_KEY = os.getenv("S3_SECRET_KEY")

app = FastAPI()
logger = logging.getLogger(__name__)

s3_resource = boto3.resource(
	"s3",
	aws_access_key_id=S3_KEY_ID,
	aws_secret_access_key=S3_SECRET_KEY,
)

BUCKET_NAME = "2022t3comp6733-smartedge"

META_FILE_EXT = ".json"

@app.get("/health")
async def health_check():
	return {"status": "OK"}

@app.get("/trips")
async def list_trips():
	bucket = None
	try:
		bucket = s3_resource.Bucket(BUCKET_NAME)
	except ClientError:
		logger.exception("Couldn't get bucket.")
		raise
	except NoCredentialsError:
		logger.exception("No credentials for bucket.")
		raise

	meta_objects = None
	try:
		meta_objects = bucket.objects.filter(Prefix="meta_")
	except ClientError:
		logger.exception("Couldn't list meta objects.")
		raise
	except NoCredentialsError:
		logger.exception("No credentials for listing meta objects.")
		raise

	resp = {"data": []}
	for obj in meta_objects:
		parts = obj.key.split("_")
		if len(parts) != 5:
			continue # skip on unexpected filename
		if parts[4].endswith(META_FILE_EXT) != True:
			continue # skip on unexpected filename
		# trip_name = parts[1] # just always "trip"
		dt = parts[2]
		lat = parts[3]
		long = parts[4].strip(META_FILE_EXT)
		resp["data"].append({
			# "name": trip_name,
			"datetime": dt,
			"latitude": lat,
			"longitude": long,
		})
	return resp

@app.get("/trips/{trip}/data")
def list_data(trip):
	bucket = None
	try:
		bucket = s3_resource.Bucket(BUCKET_NAME)
	except ClientError:
		logger.exception("Couldn't get bucket.")
		raise
	except NoCredentialsError:
		logger.exception("No credentials for bucket.")
		raise

	objects = None
	prefix = f"{trip}_"
	try:
		objects = bucket.objects.filter(Prefix=prefix)
	except ClientError:
		logger.exception(f"Couldn't list objects after {prefix}.")
		raise
	except NoCredentialsError:
		logger.exception("No credentials for listing objects.")
		raise
	
	resp = {"data": []}
	for object in objects:
		resp["data"].append(object.key)
	
	return resp


@app.get("/data/{key}")
def get_object(key):
	bucket = None
	try:
		bucket = s3_resource.Bucket(BUCKET_NAME)
	except ClientError:
		logger.exception("Couldn't get bucket.")
		raise
	except NoCredentialsError:
		logger.exception("No credentials for bucket.")
		raise

	object = None
	try:
		object = bucket.Object(key)
	except ClientError:
		logger.exception(f"Couldn't get {key}.")
		raise
	except NoCredentialsError:
		logger.exception("No credentials for getting object.")
		raise

	if key.split(".")[-1] == "mp4":
		return StreamingResponse(object.get()["Body"], media_type="video/mp4")

	body = object.get()["Body"].read()
	media_type = ""
	if key.split(".")[-1] == "jpg":
		media_type = "image/jpg"
	elif key.split(".")[-1] == "jpeg":
		media_type = "image/jpeg"
	elif key.split(".")[-1] == "png":
		media_type = "image/png"
	else:
		return Response(content=body)

	return Response(content=body, media_type=media_type)
