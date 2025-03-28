import os
import requests
from dotenv import load_dotenv

load_dotenv()


def chat_with_model(token):
    url = 'http://lambda-scalar.ad.und.edu:30000/api/chat/completions'
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    data = {
      "model": "gemma:2b",
      "messages": [
        {
          "role": "user",
          "content": "Why is the sky blue?"
        }
      ]
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()

web_ui_token = os.getenv("WEB_UI_TOKEN")
response = chat_with_model(web_ui_token)
print(response)