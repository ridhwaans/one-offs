import argparse
import ConfigParser
import os
import boto
import boto3
import StringIO
from boto.s3.key import Key
import smart_open
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter

# datalake/public/growth/staging/silver/third_party/facebook/ad_set/2017-04-12.avro
parser = argparse.ArgumentParser(description="Read file contents from S3")
parser.add_argument("bucket", type=str, help="S3 Bucket name")
parser.add_argument("key", type=str, help="S3 Key path and name")
args = parser.parse_args()

config = ConfigParser.ConfigParser()
config.read(os.environ['HOME'] + '/.aws/credentials')
access_key = config.get('default', 'aws_access_key_id')
secret_key = config.get('default', 'aws_secret_access_key')

conn = boto.connect_s3(
        aws_access_key_id = access_key,
        aws_secret_access_key = secret_key,
        #is_secure=False,               # uncomment if you are not using ssl
        )


output = StringIO.StringIO()
s3 = boto3.resource('s3')
latest_file_object = s3.Object(args.bucket,args.key)
latest_file_object.download_fileobj(output)

reader = DataFileReader(output, DatumReader())
for r in reader:
    print r
