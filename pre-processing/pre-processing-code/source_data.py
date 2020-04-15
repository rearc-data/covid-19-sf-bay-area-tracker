import datetime
import pandas as pd
import boto3

source_dataset_url = "https://docs.google.com/spreadsheets/u/1/d/1l0xahMRiLlom-7R1bHh1nWWU4DdOafShL3-8scceC3o/export?format=csv&id=1l0xahMRiLlom-7R1bHh1nWWU4DdOafShL3-8scceC3o&gid=0"

def source_dataset(new_filename, s3_bucket, new_s3_key):
	df = pd.read_csv(source_dataset_url, index_col=None)

	df.to_csv('/tmp/' + new_filename, index=False)

	#uploading new s3 dataset
	s3 = boto3.client('s3')
	s3.upload_file('/tmp/' + new_filename, s3_bucket, new_s3_key)
