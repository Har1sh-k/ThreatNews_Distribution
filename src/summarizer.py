import os
import requests
import status_logger
from dotenv import load_dotenv

load_dotenv()


def chat_with_model(content, token):
    url = 'http://lambda-scalar.ad.und.edu:30000/api/chat/completions'
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    data = {
      "model": "gemma3:27b",
      "messages": [
        {
          "role": "user",
          "content": "summarize the following news article in 3-4 lines:\n\n" + content["Title"] + "\n\n" + content["Description"] + "\n\n" + content["Link"]+ "\n\n" + "Remember : Dont write sure or anything else. Just the summary. Be as technical as possible. Use technical terms."
        }
      ]
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()

def llm_summarizer(news, web_ui_token):
  try:
    if news is None:
        return None
    for k in news:
      summary =chat_with_model(news[k], web_ui_token)
      summary = summary["choices"][0]["message"]["content"]
      #news[k]["Summary"] = summary.split("\n\n")[1]
      news[k]["Summary"] = summary
    return news
  except Exception as e:
    status_logger.debug_logger('error',f"Error in summarizing news: {e}")
    return None
    
  