import requests
from requests.auth import HTTPBasicAuth
import ConfigParser

Config = ConfigParser.ConfigParser()
Config.read("confluence.conf")
username = Config.get('credentials','username')
password = Config.get('credentials','password')
baseUrl = Config.get('instance','baseUrl')
label = Config.get('label','label')

payload =  [{"prefix": "global", "name": label}]
#contentId = 106839494

class APIError(Exception):
    """An API Error Exception"""

    def __init__(self, status):
        self.status = status

    def __str__(self):
        return "APIError: status={}".format(self.status)

f = open('contentids.out','r')
for x in f:
	contentId = x.rstrip()
	print contentId
	reqUrl = baseUrl + '/rest/api/content/' + str(contentId) + '/label'
	resp = requests.post(reqUrl, json=payload, auth=HTTPBasicAuth(username, password))
	if resp.status_code == 404:
		print "404"
	elif resp.status_code != 200:
		raise APIError(resp.status_code)
