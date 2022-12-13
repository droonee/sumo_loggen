#!/bin/bash

sudo apt update
sudo apt install python3-pip
pip install -r requirements.txt

echo "Creating service file"

sudo cat > /etc/systemd/system/loggen_test.service << EOF
[Unit]
Description=Sumo Logic log generation service

[Service]
ExecStart=/usr/bin/python3 /home/ubuntu/sumo_loggen_test/sumo_loggen_test.py
User=root
Group=root

[Install]
WantedBy=multi-user.target
EOF

echo "Reloading daemon, enable, and start service"

sudo systemctl daemon-reload
sudo systemctl enable loggen_test.service
sudo systemctl start loggen_test.service
echo "Service started"

su -l ubuntu
