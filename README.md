# Random Log Generator
Generate fake log messages for different log types

## Pre-requisites
- pip install Faker (Link to Faker Docs: https://faker.readthedocs.io/en/master/index.html)
- create an HTTP Logs and Metrics source on a hosted collector

### Steps
- install both python files for the desired log type to the same folder on your instance
- make sure you follow the prequisites to installing necessary packages
- update the sumo_endpoint variable to the http source endpoint in the *_loggen.py file
- set the *_loggen.py file to run as a service on the instance