import RSS_getter

NewsLetter_path="src/RSS_Newsletter.txt"
news,error_stack=RSS_getter.get_NEWS(NewsLetter_path)

for i in news:print(news[i]["Published_date"], news[i]["Link"])
#print(news)
print(error_stack)