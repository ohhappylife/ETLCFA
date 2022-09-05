from newscatcher import news_catcher_main
from googleNews import google_main
from politifact import politifact_main
from news import news_main

keyword = "tesla"

news_catcher_main.googleNews(keyword)
google_main.googleNews(keyword)
politifact_main.crawlit()
news_main.news(keyword)