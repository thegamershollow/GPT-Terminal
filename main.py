import os
import os.path
import openai
import datetime
import base64
import platform
import pathlib

#asks user for to allow the python script to run bash commands
consentPath = '.consent.txt'
consentCheck = os.path.isfile(".consent.txt")
if consentCheck == False:
    consent = input("Do you want to allow this python script to run bash commands? (Y/N)")
    storeConsent = open('.consent.txt', 'a')
    storeConsent.write(consent)
    storeConsent.close()
    consentYes = 'y'

#imliments an OpenAI API key from API-Key.env
apiKey = open('API-Key.env', 'r')
api = apiKey.read()
openai.api_key = api

#runs commands to install the required python modules IF consent was previously provided
cachedConsent = open('.consent.txt', 'r')
if cachedConsent == 'y':
    CurrentOS = platform.system()
    os.system("bash")
    os.system("pip install --upgrade pip")
    os.system("pip install -r requirements.txt")
    os.system("clear")

print('Starting GPT Terminal')
os.system('alias python=python3')
os.system("python3 startup.py")