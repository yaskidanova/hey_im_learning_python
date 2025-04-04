from datetime import datetime
import pytz
import json
import random
import os
import requests


#define a variable to get today's date and change the time zone 

today = datetime.now(pytz.UTC)  
chicago_tz = pytz.timezone('America/Chicago') 
chicago_time = today.astimezone(chicago_tz)


 #convert datetime object to string and take only month and day

today_str = chicago_time.strftime("%m-%d")    

#  function which chooses random message from a list 

def bd_message(slackid):
    messages = [
        f"Happy Birthday, <@{slackid}>! 🎂 Wishing you a day filled with joy and a year ahead of success and happiness!",
        f"It's <@{slackid}>'s special day! 🎉 Hope your birthday is as wonderful as you are. Enjoy every moment!",
        f"Happy Birthday to our amazing colleague <@{slackid}>! 🥳 May your day be filled with laughter and great memories!",
        f"Sending birthday wishes to <@{slackid}>! 🎁 May this year bring you everything you're hoping for and more!",
        f"It's time to celebrate <@{slackid}>! 🎈 Wishing you all the best today and throughout the coming year!"
    ]

    # using random method return a random message from the list 
    random_message = random.choice(messages)
    return random_message

# This function checks if today's date matches with any date from json file 

    
def birthdayCheck():
    data_file = "/root/Project/birthday_data.json"
    slack = os.getenv("SLACK_URL")
    headers = {"Content-type": "application/json"}

    file = open(data_file, "r")     
    content = file.read()       
    python_object = json.loads(content)         #convert this file into python format
    file.close()   
  
    for i in python_object:
        if today_str == i["db"][5:10]: 
            slack_ms = bd_message(i['slackid'])
            json_ms = json.dumps({"text": slack_ms})
            requests.post(url=slack, headers=headers, data=json_ms)   
birthdayCheck()



