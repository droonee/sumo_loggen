# Random Log Generator
Generate fake log messages for different log types using Pythons Faker library (Link to Faker Docs: https://faker.readthedocs.io/en/master/index.html)

### Prerequisites
- Launch an Ubuntu LTS 20.04 t2.medium AWS EC2 instance
       
- Create an HTTP Logs and Metrics source on a Hosted Collector in your Sumo Logic account

- Connect to EC2 instance and run 

       git clone https://github.com/droonee/sumo_loggen.git sumo_loggen && cd sumo_loggen && chmod +x setup.sh && sudo su

- Run `bash setup.sh` to install the requirements and setup the dependencies

### Steps to use
- Input the HTTP Endpoint into the sumo_loggen.py file located in the parent sumo_loggen directory

- Apache is selcted to begin logging by default.  Any time a different loggen is chosen, run the following to restart the systemd service

       sudo systemctl daemon-reload
       sudo systemctl restart loggen.service

### Cleanup
- Stop the EC2 instance when you do not need log data flowing

### Troubleshooting
- Try using receipt time when log searching

- Make sure that the absolute path to the Resources folder is accurate in the *_loggen.py file:
        
        sys.path.insert(0, '/home/ubuntu/sumo_loggen/Resources')

