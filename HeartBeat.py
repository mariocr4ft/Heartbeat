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

def startOnRun():
    print("Welcome to Heartbeat")

def checkConfig():
    if url == "":
        print("Invalid syntax in config, please check docs.")
        exit()

def runningTimer():
    checkConfig()
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Heartbeat connected correctly. Code 200.")
        else:
            print("Error connecting to the heartbeat. Please check the firewall or have this code as a reference. Code: " + str(response.status_code))
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to the heartbeat: {e}")

with open('config.json', 'r') as file:
    data = json.load(file)
    url = data['url']

# Comprobar el sistema operativo
if osType == "Linux":
    usingLinux = True
    osdistro = distro.name()
    osver = distro.version()

if not usingLinux:
    print("Hello! You are supposed to use this script with Linux only, otherwise, the script will fail.")
    print("If you think this is an error, please report it at https://github.com/mariocr4ft/Heartbeat/issues")
    exit()
else:
    startOnRun()
    print(f"You are using Linux {osdistro} version {osver}.")
    runningTimer()
    schedule.every(10).minutes.do(runningTimer)

while True:
    schedule.run_pending()
    time.sleep(1)
