import ast
import requests
import RSS_praser
from collections import defaultdict

with open('src/RSS_Newsletter.txt') as f:
    RSS_data = f.read()
RSS_data = ast.literal_eval(RSS_data)
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
    }
news = defaultdict(lambda: {
        "Title": "",
        "Description": "",
        "Published_date": "",
        "Link": "",
    })
count=0
for i in RSS_data:
    response = requests.get(RSS_data[i],headers=headers)
    url_data = response.text

    if response.status_code==200:
        news,count=RSS_praser.check_parse(url_data,news,count)
    else:
        print(response.status_code, i, RSS_data[i])

for i in news:print(news[i]["Published_date"])
#print(news)