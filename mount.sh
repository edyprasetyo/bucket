#!/bin/bash

# Set the variables
endpoint_url='https://nos.wjv-1.neo.id'
access_key_id='00bb49f84069a26c7e72'
secret_access_key='BXYiwWJzp1pQ6Iy29FMcaqVwzu71VpjLkrUX48hj'
bucket_name='edys-bucket'
mount_dir='/mnt/s3_bucket'

# Install s3fs
sudo apt-get update
sudo apt-get install s3fs

# Create the mount directory
sudo mkdir $mount_dir

# Set the directory permissions
sudo chown $USER:$USER $mount_dir

# Set up the password file
echo "${access_key_id}:${secret_access_key}" > $HOME/.passwd-s3fs
chmod 600 $HOME/.passwd-s3fs

# Mount the S3 bucket
sudo s3fs $bucket_name $mount_dir -o passwd_file=$HOME/.passwd-s3fs -o url=$endpoint_url

# Verify that the bucket is mounted
if mount | grep $mount_dir > /dev/null; then
    echo "S3 bucket $bucket_name is mounted at $mount_dir"
else
    echo "Failed to mount S3 bucket $bucket_name"
fi
