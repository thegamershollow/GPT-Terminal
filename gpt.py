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

#GPT
print('ChatGPT')
question = input("Type your prompt below (type exit to go back to selection screen):\n")
response = openai.ChatCompletion.create(
model="gpt-3.5-turbo",
messages=[{"role": "user", "content": question}]
)
if question == 'exit':
    os.system("python startup.py")

answer = response['choices'][0]['message']['content']

print('ChatGPT:\n',answer)