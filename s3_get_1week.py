import boto3
import csv
from datetime import datetime, timedelta
import uuid

# Create an S3 client
s3 = boto3.client('s3')

# Please enter following value Specify the name of the S3 bucket you want to delete versions from
bucket_name = "[YOURBUCKETNAME]]"

# Set number of days for delta 
daysbetweenversion =7

# Get a list of all the objects in the bucket
response = s3.list_objects_v2(Bucket=bucket_name)

filename = 'log/s3versionslog_' + str(uuid.uuid4()) + '.csv'
with open(filename, 'a', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['ObjectName','VersionID','LastModified','MarkedForDeleation'])




# Iterate through the objects and delete any previous versions that are less than one week older than the current version
for obj in response['Contents']:
    key = obj['Key']
    version_response = s3.list_object_versions(Bucket=bucket_name, Prefix=key)
    print("Object Name: " + key)
        
    if 'Versions' in version_response:
        # Sort the versions by date in descending order
        versions = sorted(version_response['Versions'], key=lambda x: x['LastModified'], reverse=True)
        tobeDeleted = 'No'

        
        # Get the current version's last modified date
        current_versoion = versions[0]['VersionId']
        current_version_date = versions[0]['LastModified']
        
        
        with open(filename, 'a', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow([key , current_versoion , current_version_date.strftime("%Y-%m-%d %H:%M:%S") , tobeDeleted])
        
        # print the current version - the latest version
        print(f"   --  Version ID: {versions[0]['VersionId']}   -- UpdatedOn: {versions[0]['LastModified']}")
        
        # Iterate through the previous versions and delete any that are less than one week older than the currently selected  version
        for version in versions[1:]:
            print(f"   --  Version ID: {version['VersionId']}   -- UpdatedOn: {version['LastModified']}")
            current_version = version['VersionId']
            version_date = version['LastModified']
            
            if (current_version_date - version_date) < timedelta(days=daysbetweenversion):
                print(f"         -- Marked for deletion YES ")
                tobeDeleted = 'Yes'
            else:
            # update the current version date for next comparision
                current_version_date = version['LastModified']
                tobeDeleted = 'NO'

            with open(filename, 'a', newline='') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow([key , current_version , version_date.strftime("%Y-%m-%d %H:%M:%S") , tobeDeleted])
                
print(f' Output written at file {filename}');
