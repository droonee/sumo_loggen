#!/usr/bin/python
import datetime
import time
import random
import requests
import json
import sys
import random
from faker import Faker
from tzlocal import get_localzone
sys.path.insert(0, '/home/ubuntu/sumo_loggen/Resources')
from master_provider_list import *

# sumo http source endpoint
sumo_endpoint = "<sumo endpoint>"

# initialize faker instance and add providers from apache_providers
fake = Faker()
fake.add_provider(agent_uuid)
fake.add_provider(uuid)
fake.add_provider(device_type)
fake.add_provider(fqdn)
fake.add_provider(private_ipv4)
fake.add_provider(operating_sys)
fake.add_provider(cve)
fake.add_provider(vulnerability_name)
fake.add_provider(risk)
fake.add_provider(filepath)
fake.add_provider(port)
fake.add_provider(protocol)
fake.add_provider(status)
fake.add_provider(severity_text)
fake.add_provider(severity_int)

# create the randomized tenable log
def tenable_log():
    local_time = get_localzone()
    local_time = datetime.datetime.now(local_time).strftime('%Y-%m-%dT%H:%M:%S')

    # initialize objects
    log={}
    asset={}
    plugin={}
    port={}
    scan={}

    # build asset object
    asset["agent_uuid"]=fake.agent_uuid()
    asset["device_type"]=fake.device_type()
    temp_host=fake.fqdn()
    asset["fqdn"]=temp_host
    asset["hostname"]=temp_host
    asset["uuid"]=fake.uuid()
    asset["ipv4"]=fake.private_ipv4()
    asset["operating_system"]=[fake.operating_sys()]
    asset["tracked"]=bool(random.getrandbits(1))

    # build plugin object
    plugin["checks_for_default_account"]=bool(random.getrandbits(1))
    plugin["checks_for_malware"]=bool(random.getrandbits(1))
    plugin["cve"]=[fake.cve()]
    plugin["cvss_base_score"]=round(random.uniform(0, 10), 1)
    plugin["description"]='This is a description of the vulnerabilities surfaced.'
    plugin["exploit_available"]=bool(random.getrandbits(1))
    plugin["exploited_by_malware"]=bool(random.getrandbits(1))
    plugin["exploited_by_nessus"]=bool(random.getrandbits(1))
    plugin["id"]=round(random.uniform(100000, 600000))
    plugin["name"]=fake.vulnerability_name()
    plugin["risk_factor"]=fake.risk()
    plugin["solution"]='These are the steps that you need to follow:'
    plugin["synopsis"]='The remote host has an application installed that is affected by multiple vulnerabilities.'
    plugin["version"]=round(random.uniform(0, 4), 1)

    # build port object
    port["port"]=fake.port()
    port["protocol"]=fake.protocol()

    # build scan object
    scan["completed_at"]=local_time    

    # build parent object
    log["asset"]=asset
    log["output"]=fake.filepath()
    log["plugin"]=plugin
    log["port"]=port
    log["scan"]=scan
    log["severity"]=fake.severity_text()
    log["severity_id"]=fake.severity_int()
    log["state"]=fake.status()


    json_log = json.dumps(log)
    #print(json_log)
    
    # post to sumo endpoint
    req = requests.post(sumo_endpoint, data=json_log)

    sleeptime = random.choice(range(3, 20))
    time.sleep(sleeptime)

while True:
    tenable_log()
