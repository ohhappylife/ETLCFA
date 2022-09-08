from datetime import date

import information
import transform_general.remove_stop_words
from transform_general import create_Ngram
from extract.newscatcher import news_catcher_crawler, news_transform

def googleNews(keyword):

  df = news_catcher_crawler.newsCatcher(keyword)
  df = news_transform.cleanit(df)
  df = transform_general.remove_stop_words.remove_stopwords(df)

  today = date.today()
  fname = "cleaned_news_catcher_" + str(today) + '.csv'

  information.savetoBucket(df, 'newsdata', fname)
  create_Ngram.Ngram(df, 'news_catcher' + str(today))