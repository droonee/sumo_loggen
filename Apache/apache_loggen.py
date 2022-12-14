#!/usr/bin/python
import random
import requests
import sys
import os
from faker import Faker

sys.path.insert(0, '/home/ubuntu/sumo_loggen/Resources')
from master_provider_list import *

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

def loggen(endpoint, time):
    priv_ipv4 = fake.private_ipv4()
    pub_ipv4 = fake.public_ipv4()
    method = fake.method()
    filepath = fake.filepath()
    status_code = fake.status_code()
    bytes = fake.bytes()
    uri = fake.uri()
    useragent = fake.user_agent()
    mydata = ('%s %s - - [%s] "%s %s HTTP/1.0" %s %s "%s" "%s"\n' % (priv_ipv4,
              pub_ipv4, time, method, uri, status_code, bytes, filepath, useragent))

    # post to sumo endpoint
    try:
        req = requests.post(endpoint, data=mydata)
    except:
        return
