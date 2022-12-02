# Random Log Generator
Generate fake log messages for different log types

## Prerequisites
- Launch Ubuntu LTS 20.04 t2.medium instance and connect
    
        sudo apt update
    
        sudo apt install python3-pip
    
        sudo pip install Faker (Link to Faker Docs: https://faker.readthedocs.io/en/master/index.html)

- Create an HTTP Logs and Metrics source on a hosted collector

### Steps
- Install both python files for the desired log type to the same folder on your instance
- Make sure you follow the prequisites to installing necessary packages
- Update the sumo_endpoint variable to the http source endpoint in the *_loggen.py file
- Set the *_loggen.py file to run as a service on the instance:

        Write the service:
        sudo nano /etc/systemd/system/loggen.service (name of the service which is loggen in this case)

        Paste the below and edit the filepath:
        
        ---------------------
        [Unit]
        Description=My fake log service

        [Service]
        ExecStart=/usr/bin/python3 /home/ubuntu/<path to *_loggen.py>
        User=root
        Group=root

        [Install]
        WantedBy=multi-user.target
        ---------------------

        Reload daemon:
        sudo systemctl daemon-reload

        Enable service so that it doesn’t get disabled if the server restarts:
        sudo systemctl enable loggen.service

        Start the service:
        sudo systemctl start loggen.service

        Check service status:
        sudo systemctl status loggen

### Cleanup
- stop the instance when you do not need log data flowing

### Troubleshooting
- try using receipt time when log searching