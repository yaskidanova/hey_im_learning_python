import requests, os                                 # The requests library is designed to handle HTTP requests

url = os.getenv("SERVER_URL")                          
slack = os.getenv("SLACK_URL")                      # Get the value of an environment variable
headers = {"Content-type": "application/json"}
slack_id = os.getenv("SLACK_ID")

 # This function allows to send a message to Slack with different data
def slack_sms(data):
    requests.post(url=slack, headers=headers, data=data)

# Try-except block for error handeling
try:
    response = requests.get(url)                    # Sends an HTTP request to the website and stores the server's answer in the response variable
    if response.status_code == 200:                 # Checks for success 200 means Ok (HTTP status code)
        print(f"{url} is up!")
    else:
        print(f"Oops! Status code: {response.status_code}")

except requests.exceptions.ConnectionError:         # Catches a specific error
    slack_sms(data=f'{"text": ":rotating_light: Web Server: {url} is down :ahhhhhh: -- Set By {slack_id}"}')
except:
    print(f"{url} something went wrong!")
    slack_sms(data=f'{"text": "Web Server: {url} something went wrong -- Set By {slack_id}"}')