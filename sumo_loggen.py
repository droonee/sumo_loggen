#!/usr/bin/python
import datetime
import random
import time
from tzlocal import get_localzone
from master_import import *

# add your Sumo HTTP endpoint here
HTTP_ENDPOINT = ""

while True:
    local_time = get_localzone()
    local_time = datetime.datetime.now(local_time).strftime('%Y-%m-%d %H:%M:%S')

    ### list of services to choose from - Apache is the default loggen ###
    # Apache
    # Tenable
    # ProofpointTAP

    service = Apache # modify service from the list above to generate that data 
    service.loggen(HTTP_ENDPOINT, local_time)

    sleep = random.choice(range(3,20))
    time.sleep(sleep)
