import sys
from newscatcher import news_catcher_main
from googleNews import google_main
from politifact import politifact_main
from news import news_main

try:
  keyword = sys.argv[1] # To test at the Pycharm. Please change it into 0 after the testing.
except IndexError:
  exit(-1)

try:
  catcher = sys.argv[2] # 1
  google = sys.argv[3] # 2
  politifact = sys.argv[4] #3
  news = sys.argv[5] #4

  if catcher != 0: news_catcher_main.googleNews(keyword)
  if google != 0: google_main.googleNews(keyword)
  if politifact != 0: politifact_main.crawlit()
  if news != 0: news_main.news(keyword)

except IndexError:
  news_catcher_main.googleNews(keyword)
  google_main.googleNews(keyword)
  politifact_main.crawlit()
  news_main.news(keyword)
