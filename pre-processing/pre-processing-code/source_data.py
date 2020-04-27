from urllib.request import urlopen
import boto3

def source_dataset(new_filename, s3_bucket, new_s3_key):

	source_dataset_url = 'https://docs.google.com/spreadsheets/u/1/d/1l0xahMRiLlom-7R1bHh1nWWU4DdOafShL3-8scceC3o/export?format=csv&id=1l0xahMRiLlom-7R1bHh1nWWU4DdOafShL3-8scceC3o&gid=0'
	source_csv = urlopen(source_dataset_url).read().decode().splitlines()
	save_location = '/tmp/' + new_filename

	with open(save_location, 'w', encoding='utf-8') as c:
		c.write(source_csv[0].lower().replace(' ', '_') + '\n')
		for row in source_csv[1:]:
			c.write(row + '\n')

	# uploading new s3 dataset
	s3 = boto3.client('s3')
	s3.upload_file(save_location, s3_bucket, new_s3_key)