import base64
import glob
import json
import os
from datetime import datetime

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
upload_file = ""
"""
    #TODO: read the file content and push to git
    search latest file in the current directory
    convert the file content to base64
    and connect to git with token
    push the file in the git repo

"""
datestring = str(int(datetime.now().strftime("%Y%m%d")))
current_path = os.path.join(os.path.dirname(__file__), datestring + "/*")

list_of_files = glob.glob(current_path) # * means all if need specific format then *.csv
latest_file = max(list_of_files, key=os.path.getctime)
upload_file = os.path.basename(latest_file).split('/')[-1]
print(upload_file)

# print(max_file)

file_= ""
with open(latest_file, "r") as file:
    file_ = file.read()


message_bytes = file_.encode('ascii')
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode('ascii')


payload = json.dumps({
  "message": "test_pi@test.com",
  "content": f'{base64_message}'
})

# test_file = open("_sql_user_data.json", "rb")

# This is the base URL for all Nautobot API calls
# base_url = 'https://api.github.com/repos/roysantu2002/ansible-repo/contents/_sql_user_data.json'
base_url = 'https://api.github.com/repos/roysantu2002/ansible-repo/contents/'+str(upload_file)

#
#
print(base_url)
try:
    response = requests.put(base_url, data=payload, headers=headers)
    print(response)
    if response.ok:
        print("Upload completed successfully!")
    else:
        print("Something went wrong!")
except Exception as e:
    print(e)