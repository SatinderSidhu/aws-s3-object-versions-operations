# S3 Versions Management with Python

Welcome. This code can help you find all the S3 object versions within a given bucket and check if versions are created within a week. 

## Requirements

This sample project depends on `boto3`, the AWS SDK for Python, and requires
Python 2.6.5+, 2.7, 3.3, 3.4, or 3.5. You can install `boto3` using pip:

    pip install boto3

Please change the folder name in following file 
s3_get_1week.py

    bucket_name = "[YOURBUCKETNAME]]"

You need to set up your AWS security credentials before the sample code is able
to connect to AWS. You can do this by simple running following command 


    aws configure 

It will ask you for access key and token (if you don't have it, use following code to generate it)

## Basic Configuration

You need to make sure the credentials you're using have the correct permissions to access the Amazon S3 
service. If you run into 'Access Denied' errors while running this sample, please follow the steps below.

1. Log into the [AWS IAM Console](https://console.aws.amazon.com/iam/home)
2. Navigate to the Users page.
3. Find the AWS IAM user whose credentials you're using.
4. Under the 'Permissions' section, attach the policy called 'AmazonS3FullAccess'
5. Re-run the sample. Now your user should have the right permissions to run the sample.




## 1 - Get all the object versions in a bucket

bucket name and file for you. All you need to do is run the code:

    python3 s3_list_allobjectsversions.py

Here's how the code works:

1. The code first creates an S3 client using the `boto3` library.
2. It then specifies the name of the S3 bucket you want to list versions for.
3. The `list_objects_v2()` method is used to get a list of all the objects in the bucket.
4. For each object, the code then uses the `list_object_versions()` method to get a list of all the versions of that object.
5. The code prints out the object key and the version ID for each version of the object.

Note that you'll need to have the `boto3` library installed and have the necessary AWS credentials configured in your environment for this code to work. Also, make sure to replace `'your-bucket-name'` with the name of the S3 bucket you want to list versions for.


## 2  .  List and delete previous versions of objects in an AWS S3 bucket that are less than one week older than the adjacent version:
 
bucket name and file for you. All you need to do is run the code:

    python3 s3_get_1week.py


Here's how the code works:

1. First, we import the necessary libraries and set the AWS credentials and the S3 bucket name.
2. We create an S3 client using the `boto3` library.
3. We set the time threshold for deleting previous versions to one week (7 days) using the `datetime` and `timedelta` functions.
4. We use the `list_objects_v2` function to get a list of all objects in the bucket.
5. For each object, we use the `list_object_versions` function to get a list of all the versions of the object.
6. We then iterate through the versions and check if the `LastModified` timestamp is less than the time threshold. If it is, we use the `delete_object` function to delete the version.

Note that this code assumes that versioning is enabled on the S3 bucket. If versioning is not enabled, the `list_object_versions` function will not return any results, and the code will not work as expected.

Also, make sure to replace the `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and `BUCKET_NAME` variables with your own values.

## License
Free to use with no obligation

Existing Versions 

Jan 1 - Original file 
Jan 10 - version 2 - delete 
Jan 12 - version 3 
Jan 20 - version 4 - delete 
Jan 22 - version 5
Jan 30 - version 5
