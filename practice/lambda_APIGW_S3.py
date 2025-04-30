# This lambda function will proccess the submitting data from the website and write the data to the S3 bucket 

# step #1: recieve input 
# step #2: extract the JSON data from request 
# step #3: store the data in S3
# step #4: return a response 

import json
import boto3
import os

# Initialize the S3 client outside of the handler
s3_client = boto3.client('s3')

def lambda_handler(event, context): 
    
    # Receive and parse JSON data from the HTTP request body
    data = json.loads(event['body'])
    # Specify the S3 bucket and key from environment variables
    bucket_name = os.environ.get('S3_BUCKET_NAME')
    file_key = os.environ.get('S3_FILE_KEY')
    # Store the data in S3
    s3.put_object(Bucket=bucket_name, Key=file_key, Body=json.dumps(data))
    # Construct a success response
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Data successfully stored in S3'})
        }

