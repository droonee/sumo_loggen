#!/usr/bin/python
import json
import datetime
import time
import numpy
import random
from tzlocal import get_localzone

outputfile = "apache_gen.log"

def loggen(outputfile):
    local_time = get_localzone()
    local_time = datetime.datetime.now(local_time).strftime('%Y-%m-%d %H:%M:%S')
    
    inputfile = open('./log_profile.json')
    jsonfile = json.load(inputfile)
    
    with open(outputfile, 'a') as outfile:
        priv_ipv4 = numpy.random.choice(jsonfile["private_ipv4"])
        pub_ipv4 = numpy.random.choice(jsonfile["public_ipv4"])
        method = numpy.random.choice(jsonfile["method"],p=[0.3,0.2,0.2,0.1,0.2])
        filepath = numpy.random.choice(jsonfile["filepath"])
        status_code = numpy.random.choice(jsonfile["status_code"])
        bytes = numpy.random.choice(jsonfile["bytes"],p=[0.15,0.15,0.2,0.4,0.1])
        uri = numpy.random.choice(jsonfile["uri"])
        useragent = numpy.random.choice(jsonfile["user_agent"])
        outfile.write('%s %s - - [%s] "%s %s HTTP/1.0" %s %s "%s" "%s"\n' % (priv_ipv4,pub_ipv4,local_time,method,filepath,status_code,bytes,uri,useragent))
        outfile.flush()
    
    inputfile.close()

while True:
    loggen(outputfile)
    sleeptime = random.uniform(2,20)
    time.sleep(1)
