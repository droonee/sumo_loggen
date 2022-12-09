#!/usr/bin/python
from apache_providers import *
import datetime
import time
import random
import requests
import sys
from faker import Faker
from tzlocal import get_localzone
sys.path.insert(0, '/home/ubuntu/sumo_loggen/Resources')
from master_provider_list import *

# sumo http source endpoint
sumo_endpoint = "<sumo endpoint>"

# initialize faker instance and add providers from apache_providers
fake = Faker()
fake.add_provider(private_ipv4)
fake.add_provider(public_ipv4)
fake.add_provider(status_code)
fake.add_provider(method)
fake.add_provider(uri)
fake.add_provider(user_agent)
fake.add_provider(filepath)
fake.add_provider(bytes)

# create the randomized apache log
def apache_log():
    local_time = get_localzone()
    local_time = datetime.datetime.now(local_time).strftime('%Y-%m-%d %H:%M:%S')

    priv_ipv4 = fake.private_ipv4()
    pub_ipv4 = fake.public_ipv4()
    method = fake.method()
    filepath = fake.filepath()
    status_code = fake.status_code()
    bytes = fake.bytes()
    uri = fake.uri()
    useragent = fake.user_agent()
    mydata = ('%s %s - - [%s] "%s %s HTTP/1.0" %s %s "%s" "%s"\n' % (priv_ipv4,
              pub_ipv4, local_time, method, uri, status_code, bytes, filepath, useragent))
    
    # post to sumo endpoint
    req = requests.post(sumo_endpoint, data=mydata)

    sleeptime = random.choice(range(3, 20))
    time.sleep(sleeptime)

while True:
    apache_log()
