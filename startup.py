import os
import openai
import datetime
import base64
import math

#imliments an OpenAI API key from API-Key.env
apiKey = open('API-Key.env', 'r')
api = apiKey.read()
openai.api_key = api
os.system("clear")

gptSelection = input("Select an option from below by typing the number\n1. Open ChatGPT\n2. Open Jailbroken ChatGPT\n3. Options\n4. Exit\nInput: ")

if gptSelection == '1':
    os.system("clear")
    os.system('alias python=python3')
    os.system("python gpt.py")

if gptSelection == '2':
    os.system("clear")
    os.system('alias python=python3')
    os.system("python options.py")

if gptSelection == '3':
    os.system("clear")
    os.system('alias python=python3')
    os.system("python jailbreak.py")

if gptSelection == '4':
    os.system('alias python=python3')
    print("Exited GPT Terminal")