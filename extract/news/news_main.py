from extract.news import news_transform, news_crawler
from transform_general import remove_stop_words, create_Ngram
from datetime import date
import information

def news(keyword):

  df = news_crawler.crawlData(keyword)
  if len(df)==0:
    pass
  else:
    df = news_transform.cleanit(df)
    df = remove_stop_words.remove_stopwords(df)

    today = date.today()
    fname = "cleaned_news" + str(today) + '.csv'

    information.savetoBucket(df, 'newsdata', fname)
    create_Ngram.Ngram(df, 'news' + str(today))