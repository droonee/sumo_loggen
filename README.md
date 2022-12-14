# Random Log Generator
Generate fake log messages for different log types using Pythons Faker library (Link to Faker Docs: https://faker.readthedocs.io/en/master/index.html)

## Prerequisites
- Launch an Ubuntu LTS 20.04 t2.medium AWS EC2 instance
       
- Create an HTTP Logs and Metrics source on a Hosted Collector in your Sumo Logic account

- Connect to EC2 and use `git clone https://github.com/droonee/sumo_loggen.git sumo_loggen && cd sumo_loggen && chmod +x setup.sh && sudo su`

- Use `bash setup.sh` to install the requirements and setup the dependencies

### Steps
- Input the HTTP Endpoint into the *_loggen.py file you will run

### Cleanup
- stop the instance when you do not need log data flowing

### Troubleshooting
- try using receipt time when log searching

- make sure that the absolute path to the Resources folder is accurate in the *_loggen.py file:
        
        sys.path.insert(0, '/home/ubuntu/sumo_loggen/Resources')

