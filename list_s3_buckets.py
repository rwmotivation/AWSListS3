import boto3

def list_s3_buckets():
    # Create a session using your AWS credentials
    session = boto3.Session()

    # Create an S3 client
    s3 = session.client('s3')

    # List all buckets
    response = s3.list_buckets()

    print("Existing S3 Buckets:")
    for bucket in response['Buckets']:
        print(f"  {bucket['Name']}")

if __name__ == "__main__":
    list_s3_buckets()
