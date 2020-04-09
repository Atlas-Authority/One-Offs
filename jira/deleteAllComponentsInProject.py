# Source: https://community.atlassian.com/t5/Jira-questions/is-there-a-way-to-bulk-delete-multiple-components/qaq-p/919311#M365696
# Python 2.7

import requests
import json
import getpass

# Username and password terminal input
username = raw_input('Jira Username: ')
password = getpass.getpass()

# Initiate session with requests.
s = requests.Session()

# Make initial request to grab a list of all <project> components.
r = s.get(
        url='https://<base-url>/rest/api/2/project/<project>/components',
        auth=(username, password),
        headers={'Content-Type': 'application/json'}
    )

full_list = r.json()

id_list = []

# Pull all components, and add their IDs to a list (id_list).
for comp in full_list:
    id_list.append(comp.get('id'))

# Confirm that you want to run the update.
conf_resp = raw_input('This will update ' + str(len(id_list)) + ' components. Proceed? (y/n): ')

# Using that list, delete the component.
if conf_resp == 'y':
    for id in id_list:
        id_fix = s.delete(
        url='https:///<base-url>/rest/api/2/component/' + id
        )
else:
    print 'Component update aborted.'
