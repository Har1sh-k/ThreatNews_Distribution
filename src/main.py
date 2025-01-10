import RSS_getter
import gmail_sender

NewsLetter_path="src/RSS_Newsletter.txt"
news,error_stack=RSS_getter.get_NEWS(NewsLetter_path)

gmail_sender.parse_send_news(news)
