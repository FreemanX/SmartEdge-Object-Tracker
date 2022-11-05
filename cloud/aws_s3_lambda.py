import boto3
import zipfile
from io import BytesIO

from_bucket_name = '2022t3comp6733-smartedgebucket'
to_bucket_name = '2022t3comp6733-smartedge'

def lambda_handler(event, context):
	print("invoking lambda")
	s3 = boto3.client('s3', use_ssl=False)
	s3_resource = boto3.resource('s3')
	
	from_bucket = s3_resource.Bucket(from_bucket_name)
	
	if len(event["Records"]) == 0:
		return

	zip_file = event["Records"][0]["s3"]["object"]["key"]
	print("extracting zip object", zip_file)

	zip_obj = from_bucket.Object(zip_file)
	buffer = BytesIO(zip_obj.get()["Body"].read())
	z = zipfile.ZipFile(buffer)
	for filename in z.namelist():
		fullpath = filename
		if filename.startswith("_"):
			continue # skip files that start with _
		if filename.endswith("/"):
			continue # skip files(directories) that end with /
		if len(filename.split("/")) > 2:
			continue # skip multiple hierarchies
		if len(filename.split("/")) > 1:
			filename = filename.split("/")[1]

		print("putting extracted file", filename)
		s3_resource.meta.client.upload_fileobj(
			z.open(fullpath),
			Bucket=to_bucket_name,
			Key=filename)

	# zip_obj.delete() # skip deleting to save on free tier operation quota