import boto3
import logging

from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)

def list_bucket(bucket, prefix=None):
	"""
	Lists the objects in a bucket, optionally filtered by a prefix.

	:param bucket: The bucket to query. This is a Boto3 Bucket resource.
	:param prefix: When specified, only objects that start with this prefix are listed.
	:return: The list of objects.
	"""
	try:
		if not prefix:
			objects = list(bucket.objects.all())
		else:
			objects = list(bucket.objects.filter(Prefix=prefix))
	except ClientError:
		logger.exception("Couldn't get objects for bucket '%s'.", bucket.name)
		raise
	else:
		return objects

def main():
	# s3_client = boto3.client('s3')
	s3_resource = boto3.resource('s3')
	s3_bucket = s3_resource.Bucket('2022t3comp6733-smartedgebucket')
	objects = list_bucket(s3_bucket)
	for obj in objects:
		print(obj.key)

	object_key = 'test_json.json'
	s3_object = s3_bucket.Object(object_key)
	try:
		body = s3_object.get()['Body'].read()
		print(body)
	except ClientError:
		logger.exception(
			"Couldn't get object '%s' from bucket '%s'.",
			s3_object.key,
			s3_bucket.name,
		)
		raise

if __name__ == "__main__":
	main()