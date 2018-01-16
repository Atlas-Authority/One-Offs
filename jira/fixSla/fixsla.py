import json
import requests
import logging
import datetime

try:
    import http.client as http_client
except ImportError:
# Python 2
    import httplib as http_client
    http_client.HTTPConnection.debuglevel = 1

startTime = datetime.datetime.now()

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

url="https://<BASE URL>/rest/servicedesk/1/servicedesk/sla/admin/task/destructive/reconstruct?force=true"
qbfile = open("out.txt","r")

data = []
counter = 0
for count, aline in enumerate(qbfile):
    print aline.strip()
    data.append(aline.rstrip())
    if count % 10 == 0:
        # headers = {"Cookie": "auth-openid=<For OneLogin>"}
        r = requests.post(url, json=data, headers=headers)
        del data[:]
        counter = counter + 1
        print('Run completed at: {:%H:%M:%S}'.format(datetime.datetime.now()))
        print('Total elapsed time: ' + str(datetime.datetime.now() - startTime))

qbfile.close()
