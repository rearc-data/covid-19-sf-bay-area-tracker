from urllib.request import urlopen
import boto3
from urllib.error import URLError, HTTPError

def source_dataset(new_filename, s3_bucket, new_s3_key):

	source_dataset_url = 'https://docs.google.com/spreadsheets/u/1/d/1l0xahMRiLlom-7R1bHh1nWWU4DdOafShL3-8scceC3o/export?format=csv&id=1l0xahMRiLlom-7R1bHh1nWWU4DdOafShL3-8scceC3o&gid=0'

	# throws error occured if there was a problem accessing data
	# otherwise downloads and uploads to s3

	try:
		response = urlopen(source_dataset_url)

	except HTTPError as e:
		raise Exception('HTTPError: ', e.code, new_filename)

	except URLError as e:
		raise Exception('URLError: ', e.reason, new_filename)

	else:

		data = response.read().decode().splitlines()
		file_location = '/tmp/' + new_filename

		with open(file_location, 'w', encoding='utf-8') as c:
			c.write(data[0].lower().replace(' ', '_').replace('#', '') + '\n')
			c.write('\n'.join(row for row in data[1:]))


		# uploading new s3 dataset

		s3 = boto3.client('s3')
		s3.upload_file(file_location, s3_bucket, new_s3_key)

		return [{'Bucket': s3_bucket, 'Key': new_s3_key}]