import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
  api_key=os.getenv("gpt_api_key"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "What is Machine Learning?",
        }
    ],
    model="gpt-4o-mini",
)


print(chat_completion)
