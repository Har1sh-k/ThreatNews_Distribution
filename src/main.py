import RSS_getter
import gmail_sender
import summarizer
import os
from dotenv import load_dotenv

load_dotenv()
web_ui_token = os.getenv("WEB_UI_TOKEN")

NewsLetter_path="src/RSS_Newsletter.txt"

news,error_stack=RSS_getter.get_NEWS(NewsLetter_path)

news=summarizer.llm_summarizer(news, web_ui_token)

gmail_sender.parse_send_news(news)
