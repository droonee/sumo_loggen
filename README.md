# apachegen
Generate fake Apache log messages on an Ubuntu EC2 instance.

1. Deploy an AWS EC2 Ubuntu Server 20.04 instance.  Instructions below only tested for v20.04
2. Update the Ubuntu server packages 
```
sudo apt update
```
3. Install Python 2.7.x 
```
sudo apt install python2-minimal
```
4. Check Python (2.7.x) version
```
python2 -V
```
5. See all Python versions on system - should see 3.x and 2.x
```
ls /usr/bin/python*
```
6. Add Python priority
```
sudo update-alternatives --install /usr/bin/python python /usr/bin/python2 1
```
7. Check default Python version - should see Python 3.x
```
python -V
```
8. We need to use Python 2.7.x, so change the default Python priority - follow instructions below
```
ubuntu@ip-172-31-16-7:~$ sudo update-alternatives --config python
There are 2 choices for the alternative python (providing /usr/bin/python).

  Selection    Path              Priority   Status
------------------------------------------------------------
* 0            /usr/bin/python3   2         auto mode
  1            /usr/bin/python2   1         manual mode

Press <enter> to keep the current choice[*], or type selection number: 1 
update-alternatives: using /usr/bin/python2 to provide /usr/bin/python (python) in manual mode
ubuntu@ip-172-31-16-7:~$ sudo update-alternatives --config python
There are 2 choices for the alternative python (providing /usr/bin/python).

  Selection    Path              Priority   Status
------------------------------------------------------------
  0            /usr/bin/python3   2         auto mode
* 1            /usr/bin/python2   1         manual mode

Press <enter> to keep the current choice[*], or type selection number:   
ubuntu@ip-172-31-16-7:~$ 
```
9. We should see Python 2.7.18 being used as our default Python version now
```
python -V
```
10. Let's update again
```
sudo apt update
```
11. Now we want to install pip
```
sudo apt install curl 
curl https://bootstrap.pypa.io/pip/2.7/get-pip.py --output get-pip.py
sudo python get-pip.py
```
12. Check pip version - should be 20.x
```
pip --version
```
13. Install Python package requirements for the script
```
pip install numpy
pip install Faker
pip install pytz
pip install tzlocal
```
14. Check that your Python packages are installed - should see all installed packages and their dependencies
```
pip freeze
```
15. Copy `log-gen.py` into a Python file on the Ubuntu EC2 instance
```
vi log-gen.py
(press 'i' to insert text in vi)
copy/paste the log-gen.py code from this repo into vi  
```
16. Make the new script executable
```
chmod +x log-gen.py
```
17. Run the script with options
```
python log-gen.py -o CONSOLE // this will print output to the Ubuntu EC2 console
python log-gen.py -o LOG // this will print output to a log called "access.log"
python log-gen.py -o GZ // this will print output to a gunzip file called "access.log.gz"
```
18. To stop script from running, hit `ctrl + c` in the terminal
