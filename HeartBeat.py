import requests
import os
import platform
import distro
import schedule
import time
import json


osType = platform.system()

usingLinux = False
osdistro = ""
osver = ""
url = ""

def checkConfig():
    if (data == ""):
        print("Invalid syntax in config, please check docs.")
        exit()

def runningTimer():
    checkConfig()
    response = requests.get(url)
    status_code = requests.status_codes
    if response.status_code == 200:
        print("Heartbeat connected correctly. Code 200.")
    else:
        print("Error connecting to the heartbeat. Please check the firewall or have this code as a reference. Code: "+status_code)

with open('config.json', 'r') as file:
    data = json.load(file)
    url = data['url']

if osType == "Linux":
    usingLinux = True
    osdistro = distro.name()
    osver = distro.version()

if not usingLinux:
    print("Hello! You are supposed to use this script with Linux only, otherwise, the script will fail.")
    print("If you think this is an error, please report it at https://github.com/mariocr4ft/Heartbeat/issues")
    exit()
else:
    print(f"You are using Linux {osdistro} version {osver}.")
    runningTimer
    # schedule.every(10).minutes.do(runningTimer)

while True:
    schedule.run_pending()
    time.sleep(1)

