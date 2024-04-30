# AWS SDK for Python Sample Project

A simple Python application illustrating usage of the AWS SDK for Python (also
referred to as `boto3`).

## Requirements

This sample project depends on `boto3`, the AWS SDK for Python, and requires
Python 2.6.5+, 2.7, 3.3, 3.4, or 3.5. You can install `boto3` using pip:

    pip install boto3

## Basic Configuration

You need to set up your AWS security credentials before the sample code is able
to connect to AWS. You can do this by creating a file named "credentials" at ~/.aws/ 
(`C:\Users\USER_NAME\.aws\` for Windows users) and saving the following lines in the file:

    [default]
    aws_access_key_id = <your access key id>
    aws_secret_access_key = <your secret key>

See the [Security Credentials](http://aws.amazon.com/security-credentials) page
for more information on getting your keys. For more information on configuring `boto3`,
check out the Quickstart section in the [developer guide](https://boto3.readthedocs.org/en/latest/guide/quickstart.html).

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


## 2 - Get all versions of objects in an AWS S3 bucket that are less than one week older than the current version:

bucket name and file for you. All you need to do is run the code:

    python3 s3_get_1week.py   

Here's how the code works:

1. The code first creates an S3 client using the `boto3` library.
2. It then specifies the name of the S3 bucket you want to delete versions from.
3. The `list_objects_v2()` method is used to get a list of all the objects in the bucket.
4. For each object, the code then uses the `list_object_versions()` method to get a list of all the versions of that object.
5. The code sorts the versions by date in descending order (i.e., the most recent versions first).
6. The code then gets the last modified date of the current version of the object.
7. The code iterates through the previous versions of the object and get any versions that are less than one week older than the current version.


## 3 - Delete all previous versions of objects in an AWS S3 bucket that are less than one week older than the current version:

bucket name and file for you. All you need to do is run the code:

    python3 s3_delete_1week.py    

Here's how the code works:

1. The code first creates an S3 client using the `boto3` library.
2. It then specifies the name of the S3 bucket you want to delete versions from.
3. The `list_objects_v2()` method is used to get a list of all the objects in the bucket.
4. For each object, the code then uses the `list_object_versions()` method to get a list of all the versions of that object.
5. The code sorts the versions by date in descending order (i.e., the most recent versions first).
6. The code then gets the last modified date of the current version of the object.
7. The code iterates through the previous versions of the object and deletes any versions that are less than one week older than the current version.

Note that you'll need to have the `boto3` library installed and have the necessary AWS credentials configured in your environment for this code to work. Also, make sure to replace `'your-bucket-name'` with the name of the S3 bucket you want to delete versions from.

## License
Free to use with no obligation

