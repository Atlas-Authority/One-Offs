import random
import urllib
import urllib2
import json
url = 'http://localhost:2990/jira/rest/api/2/user'
request_headers = {
  "X-Atlassian-Token": "nocheck",
  "Content-Type": "application/json",
  "Authorization": "Basic YWRtaW46YWRtaW4=" #Figure out your own for this bit
 }

for x in range(0, 10000):
  string = str(random.random()*10000000)
  params = json.dumps({
    "name": string,
    "password": "abracadabra",
    "emailAddress": string + "@example.com",
    "displayName": "Charlie of Atlassian"})
  request = urllib2.Request(url, params, headers=request_headers)
  contents = urllib2.urlopen(request).read()
  print x


# SQL to deactivate half of the users:
# update cwd_user set active = 0 where ((id % 2) = 0) AND id != 10000;
