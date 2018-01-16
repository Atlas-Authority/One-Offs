import requests
from requests.auth import HTTPBasicAuth
import re
import ConfigParser

Config = ConfigParser.ConfigParser()

Config.read("config.ini")

base_url = Config.get('system', 'url')

path = '/rest/api/space?limit=10000'

auth = HTTPBasicAuth(Config.get('credentials', 'username'), Config.get('credentials', 'password'))


r = requests.get(base_url+path, auth = auth)

JSESSIONID = r.cookies['JSESSIONID']
studiocrowdtokenkey = r.cookies['studio.crowd.tokenkey']

domain = re.search('//(.*$)',base_url).group(1)
cookies={'studio.crowd.tokenkey': studiocrowdtokenkey,
	'JSESSIONID' : JSESSIONID,
	'Domain' : domain}

r = requests.get(base_url+path, cookies = cookies)

spacekeys = set()

for i in r.json()['results']:
	if not re.match('^~',i['key']):
		spacekeys.add(i['key'])

for i in spacekeys:
	#if i.rstrip() == "TOOL":
	path = "/rest/api/space/" + i.rstrip() + "/content?depth=1"
	r = requests.get(base_url+path, cookies=cookies)
	tops = r.json()['page']
	results = tops['results']
	try:
		results[0]['id']
	except:
		print i.rstrip()
	else:
		path = '/json/listwatchers.action?pageId=' + results[0]['id']
		r = requests.get(base_url+path, cookies=cookies)
		watchers = r.json()['spaceWatchers']
		for i in watchers:
			print str(i) + " in " + str(results[0]['id'])

			#Uncomment this bit to do the actual deletion.

			#headers = {'X-Atlassian-Token' : 'no-check'}
			#path = '/json/removewatch.action?pageId=' + results[0]['id'] + "&username=" + i['name'] + "&type=space"
			#r2 = requests.post(base_url+path, cookies=cookies, headers=headers)
			#print r2