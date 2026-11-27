import os

import boto3
from botocore.exceptions import ClientError

bucket_name = os.environ["BUCKET_NAME"]
s3 = boto3.client(
    "s3",
    endpoint_url=os.environ["AWS_ENDPOINT_URL"],
    region_name=os.environ.get("AWS_REGION", "us-east-1"),
)

try:
    s3.create_bucket(Bucket=bucket_name)
    print(f"Created bucket {bucket_name}")
except ClientError as e:
    if e.response["Error"]["Code"] in ("BucketAlreadyExists", "BucketAlreadyOwnedByYou"):
        print(f"Using existing bucket {bucket_name}")
    else:
        raise
