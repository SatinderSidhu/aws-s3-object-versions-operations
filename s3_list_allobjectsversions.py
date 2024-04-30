import boto3
import uuid


# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/list_object_versions.html


# Create an S3 client
s3 = boto3.client('s3')

# Specify the name of the S3 bucket you want to list versions for
bucket_name = "academyofnaturalsience"

# Get a list of all the objects in the bucket
response = s3.list_objects_v2(Bucket=bucket_name)

# Iterate through the objects and list their versions
for obj in response['Contents']:
    key = obj['Key']
    version_response = s3.list_object_versions(Bucket=bucket_name, Prefix=key)
    
    print("Object Name: " + key)
    if 'Versions' in version_response:
        for version in version_response['Versions']:
            print(f"         --  Version ID: {version['VersionId']}")
    
    if 'DeleteMarkers' in version_response:
        for marker in version_response['DeleteMarkers']:
            print(f"        -- Delete Marker  Version ID: {marker['VersionId']}")

