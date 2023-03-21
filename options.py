import os
import openai
import datetime
import base64
import math

options = input("Select an option from below by typing the number\n1.Add API Key\n2.Remove API Key\n3.View API Key\n4.Back to Startup Menu\nInput: ")
if options == '1':
    inputedKey = input("Past your OpenAI API Key here: ")
    file = open("API-Key.env","w")
    file.write(inputedKey)
    file.close()
if options == '2':
    os.remove("API-Key.env")
if options == '3':
    file = open("API-Key.env","r")
    key = file.read()
    print('API Key: ',key)
    file.close()
if options == '4':
    os.system('bash')
    os.system('alias python=python3')
    os.system("python3 startup.py")