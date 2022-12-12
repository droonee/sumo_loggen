import os
import sys

os.system("sudo apt update")
os.system("sudo apt install python3-pip")
os.system("pip install -r requirements.txt")
os.system("export HTTP_ENDPOINT={args}".format(args=sys.argv[1]))
