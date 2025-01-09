import feedparser
from datetime import datetime, timedelta, timezone

import status_logger

def check_parse(rss_data,news,count):
    try:
        feed = feedparser.parse(rss_data)
        if feed.bozo:
            status_logger.debug_logger('error',f"Feed parsing error for {feed.feed.title}: {feed.bozo_exception}")
            return None,feed.bozo_exception
        else:
            status_logger.debug_logger('info',f"RSS feed successfully parsed for {feed.feed.title}")
            news,count=parse_feed(feed,news,count)
    except Exception as e:
        status_logger.debug_logger('error',f"Feed parsing error for {feed.feed.title}: {e}")
        return None,e
    return news,count

def parse_feed(feed,news,count):
    for entry in feed.entries:
        str_time=entry.published
        str_time=" ".join(str_time.split(" ")[1:-1])
        data_format="%d %b %Y %H:%M:%S"
        feed_date=datetime.strptime(str_time,data_format).replace(tzinfo=timezone.utc)
        current_time = datetime.now(timezone.utc)
        if (current_time - feed_date) <= timedelta(days=1):
            news[count] = {
                "Title": entry.title,
                "Description": entry.get("summary", "No description available"),
                "Published_date": str_time,
                "Link": entry.get("link","No link available"),
            }
            count+=1
    return news,count