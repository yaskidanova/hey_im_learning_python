from datetime import datetime
from now import datetime
import json
import random
import os
# import requests
from botocore.vendored import requests
import boto3
import datetime 
from dateutil import tz

# Define a variable to get today's date and change the time zone
today = datetime.now(tz.tzutc())
chicago_tz = dateutil.tz.gettz('US/Eastern') 
chicago_time = today.astimezone(chicago_tz)

# # Convert datetime object to string and take only month and day
today_str = chicago_time.strftime("%m-%d")    

# Function which chooses random message from a list 
def bd_message(slackid):
    messages = [
        f"Happy Birthday, <@{slackid}>! 🎂 Wishing you a day filled with joy and a year ahead of success and happiness!",
        f"It's <@{slackid}>'s special day! 🎉 Hope your birthday is as wonderful as you are. Enjoy every moment!",
        f"Happy Birthday to our amazing colleague <@{slackid}>! 🥳 May your day be filled with laughter and great memories!",
        f"Sending birthday wishes to <@{slackid}>! 🎁 May this year bring you everything you're hoping for and more!",
        f"It's time to celebrate <@{slackid}>! 🎈 Wishing you all the best today and throughout the coming year!"
    ]
    return random.choice(messages)

# Function that checks if today's date matches any date from the JSON file
def birthdayCheck(s3_bucket, s3_key):
    slack = os.getenv("SLACK_URL")
    headers = {"Content-type": "application/json"}

    # Initialize S3 client and download JSON content
    s3 = boto3.client('s3')
    response = s3.get_object(Bucket=s3_bucket, Key=s3_key)
    content = response['Body'].read().decode('utf-8')
    python_object = json.loads(content)
  
    for i in python_object:
        if today_str == i["db"][5:10]: 
            slack_ms = bd_message(i['slackid'])
            json_ms = json.dumps({"text": slack_ms})
            requests.post(url=slack, headers=headers, data=json_ms)   

# Lambda handler function
def lambda_handler(event, context):
    # Define bucket and file key via environment variables
    s3_bucket = os.getenv("S3_BUCKET_NAME")
    s3_key = "user_data.json"  
    birthdayCheck(s3_bucket, s3_key)
    return {
        'statusCode': 200,
        'body': json.dumps('Birthday check completed successfully.')
    }
