import sys
from newscatcher import news_catcher_main
from googleNews import google_main
from politifact import politifact_main
from news import news_main

try:
  keyword = sys.argv[1]
except IndexError:
  exit(-1)

try:
  catcher = sys.argv[2]
  google = sys.argv[3]
  politifact = sys.argv[4]
  news = sys.argv[5]

  if catcher != 0: news_catcher_main.googleNews(keyword)
  if google != 0: google_main.googleNews(keyword)
  if politifact != 0: politifact_main.crawlit()
  if news != 0: news_main.news(keyword)

except IndexError:
  news_catcher_main.googleNews(keyword)
  google_main.googleNews(keyword)
  politifact_main.crawlit()
  news_main.news(keyword)
