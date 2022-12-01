#!/usr/bin/python
import json
import datetime
import time
import random
import requests
from tzlocal import get_localzone

sumo_endpoint = "<http source endpoint>"

def apache_log():
    local_time = get_localzone()
    local_time = datetime.datetime.now(
        local_time).strftime('%Y-%m-%d %H:%M:%S')

    inputfile = open('./log_profile.json')
    jsonfile = json.load(inputfile)

    priv_ipv4 = random.choice(jsonfile["private_ipv4"])
    pub_ipv4 = random.choice(jsonfile["public_ipv4"])
    method = random.choice(jsonfile["method"])
    filepath = random.choice(jsonfile["filepath"])
    status_code = random.choice(jsonfile["status_code"])
    bytes = random.choice(jsonfile["bytes"])
    uri = random.choice(jsonfile["uri"])
    useragent = random.choice(jsonfile["user_agent"])
    mydata = ('%s %s - - [%s] "%s %s HTTP/1.0" %s %s "%s" "%s"\n' % (priv_ipv4,
              pub_ipv4, local_time, method, uri, status_code, bytes, filepath, useragent))
    req = requests.post(sumo_endpoint, data=mydata)

    sleeptime = random.choice(range(3, 20))
    time.sleep(sleeptime)

    inputfile.close()

while True:
    apache_log()
