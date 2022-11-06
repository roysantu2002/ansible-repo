import base64
import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()

# Get the API token from an environment variable
token = os.environ.get('git_token')

# Add the Authorization header
headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
    }

file_ = ""
file_base64 = ""

"""
    #TODO: read the file content and push to git

"""
file_=""
with open("_sql_user_data.json", "r") as file:
    file_ = file.read()

print(file_)
message_bytes = file_.encode('ascii')
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode('ascii')


payload = json.dumps({
  "message": "test_pi@test.com",
  "content": f'{base64_message}'
})

print(payload)

# test_file = open("_sql_user_data.json", "rb")

# This is the base URL for all Nautobot API calls
# base_url = 'https://api.github.com/repos/roysantu2002/ansible-repo/contents/_sql_user_data.json'
base_url = 'https://api.github.com/repos/roysantu2002/ansible-repo/contents/_sql_user_data_02.json'

#
#
# print(body)
try:
    response = requests.put(base_url, data=payload, headers=headers)
    print(response)
    if response.ok:
        print("Upload completed successfully!")
        print(response.text)
    else:
        print("Something went wrong!")
except Exception as e:
    print(e)