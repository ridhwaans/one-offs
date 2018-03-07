import argparse
import ConfigParser
import os
import boto
from boto.s3.key import Key
import smart_open


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
bucket = conn.get_bucket(args.bucket)

#key = Key(bucket, 'public/growth/staging/silver/third_party/facebook/ad_set/2017-04-12.avro')
key = Key(bucket, args.key)
print(key.get_contents_as_string())
#uri = "s3://" + access_key + ":" + secret_key + "@datalake/public/growth/staging/silver/third_party/facebook/ad_set/2017-04-12.avro"
#help(smart_open.smart_open_lib)
#for line in smart_open.smart_open(uri):
#	print line