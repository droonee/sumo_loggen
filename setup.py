import os

os.system("sudo apt update")
os.system("sudo apt install python3-pip")
os.system("pip install -r requirements.txt")
os.system("echo 'export HTTP_ENDPOINT={args}' >> ~/.bashrc".format(args=sys.argv[1]))
