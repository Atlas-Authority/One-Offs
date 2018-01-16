import requests
from requests.auth import HTTPBasicAuth
import ConfigParser
import pickle

Config = ConfigParser.ConfigParser()
Config.read("jira.conf")
username = Config.get('credentials','username')
password = Config.get('credentials','password')
baseUrl = Config.get('instance','baseUrl')
permissionDict = {}


f = open('browsePermissions.csv','w')
f.write('email,pkey\n')

projects = []

class APIError(Exception):
    """An API Error Exception"""

    def __init__(self, status):
        self.status = status

    def __str__(self):
        return "APIError: status={}".format(self.status)

reqUrl = baseUrl + '/rest/api/2/project'
resp = requests.get(reqUrl, auth=HTTPBasicAuth(username, password))
#https://docs.atlassian.com/jira/REST/6.4.6/#api/2/project-getProject
if resp.status_code != 200:
	raise APIError(resp.status_code)
for project in resp.json():
	print(project['key'])
	projects.append(project['key'])

for project in projects:
	print(project)
	startNumber = 0
	while True:
		reqUrl = baseUrl + '/rest/api/2/user/permission/search?permissions=BROWSE&maxResults=1000&username&projectKey=' + project + '&startAt=' + str(startNumber)
		# https://docs.atlassian.com/jira/REST/6.4.6/#api/2/user-findUsersWithAllPermissions
		startNumber = startNumber+1000
		resp = requests.get(reqUrl, auth=HTTPBasicAuth(username, password))
	 	if resp.status_code != 200:
			raise APIError(resp.status_code)
		if len(resp.json()) == 0:
			break
		for person in resp.json():
			if person['active']:
				email = str(person['emailAddress'])
				if permissionDict.has_key(email):
					print permissionDict[email]
					permissionDict[email].append(project)
					print email + ' ' + str(permissionDict[email])
				else :
					permissionDict[email] = [project]
				f.write(email+','+project+'\n')

f.close()
pickle.dump(permissionDict, open( "permissionDict.p", "wb"))
