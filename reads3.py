
import boto3

# ---- AWS Config ----
AWS_REGION = "ap-south-1"              # change if needed
BUCKET_NAME = "at-mytestbucket"       # replace with your bucket

def list_files():
    s3 = boto3.client("s3", region_name=AWS_REGION)

    response = s3.list_objects_v2(Bucket=BUCKET_NAME)

    if "Contents" not in response:
        print("Bucket is empty or not found.")
        return

    print(f"Files in S3 bucket '{BUCKET_NAME}':\n")
    for obj in response["Contents"]:
        print(obj["Key"])

if __name__ == "__main__":
    list_files()
