import json
import boto3
from botocore.exceptions import ClientError
import os

s3_client = boto3.client('s3')

def update_user_list(users, new_user):
    updated = False

    for i, user in enumerate(users):
        if user.get("name") == new_user.get("name"):
            users[i] = new_user
            updated = True
            break

    if not updated:
        users.append(new_user)

    return users


def lambda_handler(event, context):


    bucket_name = os.environ.get('S3_BUCKET_NAME')
    file_key = os.environ.get('S3_FILE_KEY')
    new_user = event

    try:
        old_data = s3_client.get_object(Bucket=bucket_name, Key=file_key)
        content_json = old_data['Body'].read().decode('utf-8')
        old_users_list = json.loads(content_json)


        updated = update_user_list(old_users_list, new_user)

        s3_client.put_object(Bucket=bucket_name, Key=file_key, Body=json.dumps(updated))
    except ClientError as e:
        if e.response['Error']['Code'] == 'NoSuchKey':
            print("File does not exist. Creating new file.")
            users = []
        else:
            print("Unexpected error:", e)
