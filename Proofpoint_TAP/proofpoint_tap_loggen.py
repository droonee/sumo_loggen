#!/usr/bin/python
import datetime
import time
import random
import requests
import json
import sys
import os
import random
import hashlib
from faker import Faker
from tzlocal import get_localzone

sys.path.insert(0, '/home/ubuntu/sumo_loggen/Resources')
from master_provider_list import *

# utilizing the sumo http source endpoint set as global environment variable
#sumo_endpoint = os.environ.get('HTTP_ENDPOINT')
sumo_endpoint = <http_endpoint>

# initialize faker instance and add providers from apache_providers
fake = Faker()
fake.add_provider(uuid)
fake.add_provider(email)
fake.add_provider(filename)
fake.add_provider(private_ipv4)
fake.add_provider(email_threat_class)
fake.add_provider(email_threat_type)
fake.add_provider(email_threat_subject)


# create the randomized proofpoint TAP log and duplicates
def proofpoint_log():
    local_time = get_localzone()
    local_time = datetime.datetime.now(local_time).strftime('%Y-%m-%dT%H:%M:%S')

    # initialize objects
    log={}
    message_part_1={}
    message_part_2={}
    threats_info_map1={}
    threats_info_map2={}

    # build child objects
    message_part_1["contentType"]=fake.mime_type()
    message_part_1["disposition"]="inline"
    message_part_1["filename"]=fake.filename()
    message_part_1["md5"]=hashlib.md5(message_part_1["filename"].encode()).hexdigest()
    message_part_1["oContentType"]=message_part_1["contentType"]
    message_part_1["sandboxStatus"]="unsupported"
    message_part_1["sha256"]=hashlib.sha256(message_part_1["filename"].encode()).hexdigest()

    message_part_2["contentType"]=fake.mime_type()
    message_part_2["disposition"]="inline"
    message_part_2["filename"]=fake.filename()
    message_part_2["md5"]=hashlib.md5(message_part_2["filename"].encode()).hexdigest()
    message_part_2["oContentType"]=message_part_2["contentType"]
    message_part_2["sandboxStatus"]="threat"
    message_part_2["sha256"]=hashlib.sha256(message_part_2["filename"].encode()).hexdigest()

    threats_info_map1["campaignId"]=fake.uuid()
    threats_info_map1["classification"]=fake.email_threat_class()
    threats_info_map1["threat"]="2fab740f143fc1aa4c1cd0146d334c5593b1428f6d062b2c406e5efe8abe95ca"
    threats_info_map1["threatId"]="2fab740f143fc1aa4c1cd0146d334c5593b1428f6d062b2c406e5efe8abe95ca"
    threats_info_map1["threatStatus"]="active"
    threats_info_map1["threatType"]=fake.email_threat_type()
    threats_info_map1["threatUrl"]="https://threatinsight.proofpoint.com/"

    threats_info_map2["campaignId"]=fake.uuid()
    threats_info_map2["classification"]=fake.email_threat_class()
    threats_info_map2["threat"]="badsite.zz"
    threats_info_map2["threatId"]="3ba97fc852c66a7ba761450edfdfb9f4ffab74715b591294f78b5e37a76481aa"
    threats_info_map2["threatStatus"]="active"
    threats_info_map2["threatType"]=fake.email_threat_type()
    threats_info_map2["threatUrl"]="https://threatinsight.proofpoint.com/"

    # build parent object
    log["GUID"]=str(fake.uuid())
    log["QID"]="r2FNwRHF004109"
    log["ccAddresses"]=[fake.email(), fake.email()]
    log["clusterId"]="pharmtech_hosted"
    log["completelyRewritten"]=str(bool(random.getrandbits(1))).lower()
    log["fromAddress"]=fake.email()
    log["headerCC"]="\"Bruce Wayne\" <bruce.wayne@university-of-education.zz>"
    log["headerFrom"]="\"A. Badguy\" <badguy@evil.zz>"
    log["headerReplyTo"]=None
    log["headerTo"]="\"Clark Kent\" <clark.kent@pharmtech.zz>; \"Diana Prince\" <diana.prince@pharmtech.zz>"
    log["impostorScore"]=round(random.uniform(0, 100))
    log["malwareScore"]=round(random.uniform(0, 100))
    log["messageID"]="20160624211145.62086.mail@evil.zz"
    log["messageParts"]=[message_part_1,message_part_2]
    log["messageTime"]=local_time
    log["modulesRun"]=["pdr","sandbox", "spam", "urldefense"]
    log["phishScore"]=round(random.uniform(0, 100))
    log["policyRoutes"]=["default_inbound","executives"]
    log["quarantineFolder"]="Attachment Defense"
    log["quarantineRule"]="module.sandbox.threat"
    log["recipient"]=[fake.email()]
    log["replyToAddress"]=None
    log["sender"]=fake.email()
    log["senderIP"]=fake.private_ipv4()
    log["spamScore"]=round(random.uniform(0, 100))
    log["subject"]=fake.email_threat_subject()
    log["threatsInfoMap"]=[threats_info_map1,threats_info_map2]
    log["toAddress"]=[log["recipient"]]
    log["xmailer"]="Spambot v1"


    json_log_full = json.dumps(log)
    print(json_log_full)
    json_log_message_part_1 = json.dumps(message_part_1)
    print(json_log_message_part_1)
    json_log_message_part_2 = json.dumps(message_part_2)
    print(json_log_message_part_2)
    
    # post to full log to sumo endpoint
    req = requests.post(sumo_endpoint, data=json_log_full)

    # post individual message parts to sumo endpoint
    req2 = requests.post(sumo_endpoint, data=json_log_message_part_1)
    req3 = requests.post(sumo_endpoint, data=json_log_message_part_2)


    sleeptime = random.choice(range(3, 20))
    time.sleep(sleeptime)

while True:
    proofpoint_log()
