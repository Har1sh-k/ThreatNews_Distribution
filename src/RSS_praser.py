import feedparser
from collections import defaultdict
from datetime import datetime, timedelta, timezone

def check_parse(rss_data,news,count):
    try:
        feed = feedparser.parse(rss_data)
        if feed.bozo:
            print(f"Error in parsing feed: {feed.bozo_exception}")
        else:
            print(f"RSS feed successfully parsed for {feed.feed.title}")
            news,count=parse_feed(feed,news,count)
    except Exception as e:
        print(f"An error occurred: {e}")
    return news,count

def parse_feed(feed,news,count):
    for entry in feed.entries:
        str_time=entry.published
        str_time=" ".join(str_time.split(" ")[1:-1])
        data_format="%d %b %Y %H:%M:%S"
        feed_date=datetime.strptime(str_time,data_format).replace(tzinfo=timezone.utc)
        current_time = datetime.now(timezone.utc)
        if timedelta(0) <= (current_time - feed_date) <= timedelta(days=2):
            news[count] = {
                "Title": entry.title,
                "Description": entry.get("summary", "No description available"),
                "Published_date": entry.get("published", "No date available"),
                "Link": entry.get("link","No link available"),
            }
            count+=1
    return news,count