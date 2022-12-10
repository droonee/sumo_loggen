# Random Log Generator
Generate fake log messages for different log types using Pythons Faker library (Link to Faker Docs: https://faker.readthedocs.io/en/master/index.html)

## Prerequisites
- Launch an Ubuntu LTS 20.04 t2.medium AWS EC2 instance
       
- Create an HTTP Logs and Metrics source on a Hosted Collector in your Sumo Logic account

- Connect to EC2 and use `git clone https://github.com/droonee/sumo_loggen.git sumo_loggen && cd sumo_loggen`

- Use `python3 setup.py <http_endpoint>` to install the requirements and setup the dependencies

- Use `source ~/.bashrc` to refresh the global variable.  Test with `echo $HTTP_ENDPOINT` to verify the global variable is set

### Steps
- Update the sumo_endpoint variable to the http source endpoint in the *_loggen.py file **David took care of this with global env variable**
- Set the *_loggen.py file to run as a service on the instance: **David to write code that runs from parent script where command line argument specifies the log type you want to generate - will be able to automate the systemd service setup with this change**

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

- make sure that the absolute path to the Resources folder is accurate in the *_loggen.py file:
        
        sys.path.insert(0, '/home/ubuntu/sumo_loggen/Resources')

