import boto3
from botocore.exceptions import NoCredentialsError
import json

def create_and_configure_s3_bucket(bucket_name, region='us-east-1'):
    """
    Create a new S3 bucket, upload an index.html file, configure the bucket for static website hosting,
    and set the necessary permissions for public access.

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

        # Upload index.html file
        s3.upload_file("index.html", bucket_name, "index.html")
        print("index.html uploaded successfully.")

        # Configure bucket for static website hosting
        s3.put_bucket_website(
            Bucket=bucket_name,
            WebsiteConfiguration={
                'IndexDocument': {'Suffix': 'index.html'},
                'ErrorDocument': {'Key': 'error.html'}
            }
        )
        print(f"Bucket '{bucket_name}' configured for static website hosting.")

        # Set bucket ACL for public read access
        s3.put_bucket_acl(Bucket=bucket_name, ACL='public-read')
        print("Bucket ACL set for public read access.")

        # Get website endpoint
        website_endpoint = f"http://{bucket_name}.s3-website-{region}.amazonaws.com"
        print(f"Static website URL: {website_endpoint}")
    except NoCredentialsError:
        print("Credentials not available. Please configure your AWS credentials.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Specify your desired S3 bucket name
    new_bucket_name = "45214514753"

    # Specify the AWS region where you want to create the bucket (optional, default is 'us-east-1')
    aws_region = "us-west-1"

    # Create and configure the S3 bucket for static website hosting
    create_and_configure_s3_bucket(new_bucket_name, aws_region)
