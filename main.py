import boto3
from botocore.exceptions import NoCredentialsError

def create_s3_bucket(bucket_name, region='us-east-1'):
    """
    Create a new S3 bucket in the specified AWS region.

    :param bucket_name: The desired name for the new bucket.
    :param region: The AWS region where the bucket will be created. Default is 'us-east-1'.
    """
    # Create an S3 client
    s3 = boto3.client('s3', region_name=region)

    try:
        # Create S3 bucket with location constraint
        if region != 'us-east-1':
            location = {'LocationConstraint': region}
            s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)
        else:
            s3.create_bucket(Bucket=bucket_name)

        print(f"S3 bucket '{bucket_name}' created successfully in region '{region}'.")
    except NoCredentialsError:
        print("Credentials not available. Please configure your AWS credentials.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Specify your desired S3 bucket name
    new_bucket_name = "0783914072839"

    # Specify the AWS region where you want to create the bucket (optional, default is 'us-east-1')
    aws_region = "us-west-1"

    # Create the S3 bucket
    create_s3_bucket(new_bucket_name, aws_region)
