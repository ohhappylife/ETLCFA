import sys
from extract.newscatcher import news_catcher_main
from extract.googleNews import google_main
from extract.politifact import politifact_main
from extract.news import news_main
from extract.NYTimes import NYTimes_main
from logger import logger

try:
  keyword = sys.argv[1]  # To test at the Pycharm. Please change it into 0 after the testing.
except IndexError:
  logger.critical("No keyword is given")
  exit(-1)

try:
  catcher = sys.argv[2]  # 1
  google = sys.argv[3]  # 2
  politifact = sys.argv[4]  # 3
  news = sys.argv[5]  # 4
  NYTtimes = sys.argv[6]  # 5

  if catcher != 0:
    news_catcher_main.googleNews(keyword)
    logger.debug("Crawl News Catcher")
  if google != 0:
    google_main.googleNews(keyword)
    logger.debug("Crawl Google News")
  if politifact != 0:
    politifact_main.crawlit()
    logger.debug("Crawl Poltifiact")
  if news != 0:
    news_main.news(keyword)
    logger.debug("Crawl News API")
  if NYTtimes != 0:
    NYTimes_main.crawlit(keyword)
    logger.debug("Crawl NYTimes")

except IndexError:
  logger.debug("Crawl from ALL sources")
  news_catcher_main.googleNews(keyword)
  google_main.googleNews(keyword)
  politifact_main.crawlit()
  news_main.news(keyword)
  NYTimes_main.crawlit(keyword)
