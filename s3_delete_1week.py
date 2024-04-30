import boto3
from datetime import datetime, timedelta

# Create an S3 client
s3 = boto3.client('s3')

# Specify the name of the S3 bucket you want to delete versions from
bucket_name = "academyofnaturalsience"

# Get a list of all the objects in the bucket
response = s3.list_objects_v2(Bucket=bucket_name)

# Iterate through the objects and delete any previous versions that are less than one week older than the current version
for obj in response['Contents']:
    key = obj['Key']
    version_response = s3.list_object_versions(Bucket=bucket_name, Prefix=key)
    
    if 'Versions' in version_response:
        # Sort the versions by date in descending order
        versions = sorted(version_response['Versions'], key=lambda x: x['LastModified'], reverse=True)
        
        # Get the current version's last modified date
        current_version_date = versions[0]['LastModified']
        
        # Iterate through the previous versions and delete any that are less than one week older than the current version
        for version in versions[1:]:
            version_date = version['LastModified']
            if (current_version_date - version_date) < timedelta(days=7):
                s3.delete_object(Bucket=bucket_name, Key=key, VersionId=version['VersionId'])
                print(f"Deleted object {key}, version {version['VersionId']}")
