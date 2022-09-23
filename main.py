import sys
from extract.newscatcher import news_catcher_main
from extract.googleNews import google_main
from extract.politifact import politifact_main
from extract.news import news_main
from extract.NYTimes import NYTimes_main
from logger import logger
from extract.bingNews import bing_main
import pandas as pd
from datetime import date
from transform_general import other
import information

logger.debug("start the process")

try:
  keyword = sys.argv[1]  # To test at the Pycharm. Please change it into 0 after the testing.
  logger.debug("Received Keyword : " + str(keyword))
except IndexError:
  logger.critical("err 001: No keyword is given")
  exit(-1)

try:
  catcher = sys.argv[2]  # 1
  google = sys.argv[3]  # 2
  politifact = sys.argv[4]  # 3
  news = sys.argv[5]  # 4
  NYTtimes = sys.argv[6]  # 5
  Bing = sys.argv[7] #6

  if catcher != 0:
    dfnc  =news_catcher_main.googleNews(keyword)
    logger.debug("Crawl News Catcher")
  if google != 0:
    dfg = google_main.googleNews(keyword)
    logger.debug("Crawl Google News")
  if politifact != 0: # Politifact does not support keyword search.
    dfp = politifact_main.crawlit()
    logger.debug("Crawl Poltifiact")
  if news != 0:
    dfn = news_main.news(keyword)
    logger.debug("Crawl News API")
  if NYTtimes != 0:
    dfny = NYTimes_main.crawlit(keyword)
    logger.debug("Crawl NYTimes")
  if Bing != 0:
    dfb = bing_main.bingNews(keyword)
    logger.debug('Crawl Bing news')


except IndexError:
  logger.debug("Crawl from ALL sources")
  dfp = politifact_main.crawlit()
  dfnc = news_catcher_main.googleNews(keyword)
  dfg = google_main.googleNews(keyword)
  dfn = news_main.news(keyword)
  dfny = NYTimes_main.crawlit(keyword)
  dfb = bing_main.bingNews(keyword)
today = date.today()
df = pd.concat([dfp, dfnc, dfg, dfn, dfny, dfb]) # concat the crawled data
df = other.resolveEncodeIssue(df) # resolve some encode issues; temporary method
df = df.reset_index(drop = True)

fname = "merged_" + str(today) + '.csv'
information.savetoBucket(df, 'newsdata', fname)

logger.debug("end the process")

