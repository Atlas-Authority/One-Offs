# This is for Cloud
# If you have more than 10k spaces, run this multiple times

import ConfigParser
import re

import requests
from requests.auth import HTTPBasicAuth

Config = ConfigParser.ConfigParser()

Config.read("config.ini")

base_url = Config.get('system', 'url')

path = '/wiki/rest/api/space?limit=10000'

auth = HTTPBasicAuth(Config.get('credentials', 'username'), Config.get('credentials', 'password'))

r = requests.get(base_url+path, auth = auth)

for i in r.json()['results']:
	path = "/wiki/rest/api/space/{spaceKey}" + i['key'].rstrip()
	r = requests.delete(base_url+path, auth = auth)
	print(r.text)
	