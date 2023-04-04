from datetime import timedelta
import boto3
import os

endpoint_url = 'https://nos.wjv-1.neo.id'
access_key_id = '00bb49f84069a26c7e72'
secret_access_key = 'BXYiwWJzp1pQ6Iy29FMcaqVwzu71VpjLkrUX48hj'
bucket_name = 'edys-bucket'

s3 = boto3.client('s3', aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key, endpoint_url=endpoint_url)

s3.create_bucket(Bucket=bucket_name)

file_name = 'azure.tar.gz'
file_size_in_mb = round(os.path.getsize(file_name)/1024/1024, 2)
totaluploadMB = 0
def upload_progress_callback(bytes_uploaded):
    global totaluploadMB
    totaluploadMB += bytes_uploaded/1024/1024
    print('Progress:', round(totaluploadMB/file_size_in_mb*100, 2), '%')

# s3.upload_file(file_name, bucket_name, file_name, Callback=upload_progress_callback)

# s3.download_file(bucket_name, file_name, 'downloaded-' + file_name)

response = s3.list_objects_v2(Bucket=bucket_name)
totalBucketSize = 0
for obj in response['Contents']:
    totalBucketSize += obj['Size']
    last_modified_gmt_07_00 = obj['LastModified'] + timedelta(hours=7)
    last_modified = last_modified_gmt_07_00.strftime('%Y-%m-%d %H:%M:%S')
    print(obj['Key'], round(obj['Size']/1024, 2), 'KB', last_modified)

print('Total Bucket Size:', round(totalBucketSize/1024/1024, 2), 'MB')