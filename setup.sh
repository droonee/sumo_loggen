#!/bin/bash

sudo apt update
sudo apt install python3-pip
pip install -r requirements.txt

echo "Creating service file"

sudo cat > /etc/systemd/system/loggen.service << EOF
[Unit]
Description=Sumo Logic log generation service

[Service]
ExecStart=/usr/bin/python3 /home/ubuntu/sumo_loggen/sumo_loggen.py
User=root
Group=root

[Install]
WantedBy=multi-user.target
EOF

echo "Reloading daemon, enable, and start service"

sudo systemctl daemon-reload
sudo systemctl enable loggen.service
sudo systemctl start loggen.service
echo "Service started"

su -l ubuntu
