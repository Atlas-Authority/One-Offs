# sourced from AG

import requests
import json
import sys
import getpass

# Base URL
baseUrl = "https://my-jira.com"

# List of filters to add permission to 
filters = [12345, 23456]

# Permission change params, format below
permission = {
    "type": "user",
    "userKey": "charlie_atlassian",
    "view": True,
    "edit": True
  }

'''
Group permissions

  {
    "type": "group",
    "groupname": "groupname",
    "view": true,
    "edit": false
  }

User permissions

  {
    "type": "user",
    "userKey": "userKey",
    "view": true,
    "edit": true
  }
'''

username = input('Jira Username: ')
password = getpass.getpass()

data = json.dumps(permission)

s = requests.Session()

for foo in filters:
	r = s.post(
	        url=baseUrl + "/rest/api/2/filter/" + str(foo) + "/permission",
	        data=data,
	        auth=(username, password),
	        headers={'Content-Type': 'application/json'}
	    )

	status_code = r.status_code

	# Prevents trying to run the loop with bad creds causing CAPTCHA lockout
	if status_code == 401:
	    sys.exit("Invalid credentials provided, please check username/password")
