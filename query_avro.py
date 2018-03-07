import os
import boto
from boto.s3.key import Key
import ConfigParser
import smart_open
import argparse
from pyspark.sql import SQLContext
from pyspark.sql.dataframe import DataFrame
from pyspark import SparkConf, SparkContext
from pyspark import sql

def main():
    # parser = argparse.ArgumentParser(description="Read file contents from S3")
    # parser.add_argument("bucket", type=str, help="S3 Bucket name")
    # parser.add_argument("key", type=str, help="S3 Key path and name")
    # args = parser.parse_args()

    # config = ConfigParser.ConfigParser()
    # config.read(os.environ['HOME'] + '/.aws/credentials')
    # access_key = config.get('default', 'aws_access_key_id')
    # secret_key = config.get('default', 'aws_secret_access_key')

    # conn = boto.connect_s3(
    #         aws_access_key_id = access_key,
    #         aws_secret_access_key = secret_key,
    #         #is_secure=False,               # uncomment if you are not using ssl
    #         )   
    # bucket = conn.get_bucket(args.bucket)

    # #key = public/growth/staging/silver/third_party/facebook/ad_set/2017-04-12.avro
    # key = Key(bucket, args.key)
    # print(key.get_contents_as_string())


# df = SQLContext.read.format("com.databricks.spark.avro").load("src/test/resources/episodes.avro")

# #  Saves the subset of the Avro records read in
# subset = df.where("doctor > 5")
# subset.write.format("com.databricks.spark.avro").save("/tmp/output")

    conf = SparkConf()
    conf.setMaster('local')
    conf.setAppName('SQLApiDemo')
    sc = SparkContext(conf = conf)
    print sc.version

    sqlContext = sql.SQLContext(sc)

    sqlContext.sql("CREATE TEMPORARY TABLE table_name USING com.databricks.spark.avro OPTIONS (path '/Users/ridshakeel/Downloads/2017-04-24.avro')")
    df = SQLContext.sql("SELECT COUNT(*) FROM table_name")
    df.collect()
    DataFrame df = sqlContext.load("/Users/tariq/avro_data/browser.avro/", "com.databricks.spark.avro");

if __name__ == "__main__":
    main()