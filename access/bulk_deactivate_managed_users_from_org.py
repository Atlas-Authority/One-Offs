# Please be aware that these scripts are not officially supported by Atlassian Support. They utilize internal unpublished APIs which have more restricted rate limiting rules and could change at any time. They're are best used in batches of smaller lists of users.
# Your organization ID: you can get this on the URL of your org e.g https://admin.atlassian.com/o/<ORG ID IS HERE>/overview
# Org admin API key: here is a guide on creating admin APIs keys.
# The file that lists the email addresses of the users. One user per line. e.g a .csv or .txt file
# python3 bulk_deactivate_managed_users_from_org.py <organization-id> <org-admin-api-key> <list-of-user.txt>


import sys, argparse, requests, json, browser_cookie3
from datetime import datetime
from csv import reader

def main():
	
    parser = argparse.ArgumentParser(description='Bulk deactivate users from an Atlassian Organisation')
    parser.add_argument('org_id', type=str, help='Unique ID of the Atlassian Organisation')
    parser.add_argument('org_api_key', type=str, help='API key created at the Org level')
    parser.add_argument('users_to_deactivate_file', type=str, help='File contains eamil address of the users. One user per line.')
    args = parser.parse_args()
    
    user_cookies = browser_cookie3.chrome()
    
    print('{} - Initiated Account deactivate Process.....'.format(datetime.now()))

    deactivate_users=[]
    with open(args.users_to_deactivate_file, 'r') as read_users:
        for u in read_users:
            deactivate_users.append(u.strip().lower())

    # Get Atlassian Account ID of the each User
    aa_ids = get_user_aaid(args.org_id, args.org_api_key, deactivate_users)
    #print(aa_ids)
    #print(*aa_ids, sep = "\n")

    # Now deactivate Atlassian Account of each user
    for user in aa_ids:
        if user["status"]!='closed':
            print('{} - deactivating User: {} [{}]'.format(datetime.now(),user["email"],user["aa_id"]))
            deactivate_user(user_cookies, user["aa_id"])
        else:
            print('{} - User: {} [{}] is already deactivated. No action required.'.format(datetime.now(),user["email"],user["aa_id"]))

    print('{} - Finished Account deactivate Process....'.format(datetime.now()))

def get_user_aaid(orgId, orgApiKey, usersList):
    orgUsers = []
    requestUrl = "https://api.atlassian.com/admin/v1/orgs/{}/users".format(orgId)

	# Set the HTTP headers for the request
    headers = {
	   "Accept": "application/json",
	   "Authorization": "Bearer " + orgApiKey
	}
    
    sys.stdout.write("{} - Getting Users Atlassian Accounts IDs\n".format(datetime.now()))

	# Execute the HTTP request
    while True:
        response = requests.request(
            "GET",
            requestUrl,
            headers=headers
		)

		# Deserialize the response text as JSON
        responseJson = json.loads(response.text)
        
        for i in responseJson["data"]:
            if i["email"].lower() in usersList:
                orgUsers.append({'aa_id':i["account_id"],'email':i["email"].lower(),'status':i["account_status"]})
       

		# If there is pagination, re-define the requestUrl to the next page from the cursor
        if 'next' in list(responseJson["links"]):
            requestUrl = responseJson["links"]["next"]
        else:
            break

    return orgUsers

def deactivate_user(user_cookie, userAAID):
    
    requestUrl = "https://admin.atlassian.com/gateway/api/users/{}/deactivate".format(userAAID)
    
    # REST API call
    response = requests.post(
        requestUrl,
        cookies = user_cookie
    )
    
    if response.status_code == 204:
        sys.stdout.write('{} - SUCCESS: Atlassian Account [{}] has been deactivated\n'.format(datetime.now(), userAAID))
    else:
       sys.stdout.write('{} - ERROR: Atlassian Account [{}] cannot be deactivated. Response: {}\n'.format(datetime.now(), userAAID, response.text))

if __name__ == "__main__":
        main()
