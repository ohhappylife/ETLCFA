from datetime import date

import information
import transform_general.remove_stop_words
from transform_general import create_Ngram
from extract.newscatcher import news_catcher_crawler, news_transform

def googleNews(keyword):
  """
  collect news from Google News based on a keyword and clean it.
  :param str keyword: collected news articles and transform articles based on keyword.
  :return: cleaned news articles
  :rtype: dataframe
  """
  df = news_catcher_crawler.newsCatcher(keyword)
  if len(df) ==0:
    pass
  else:
    df = news_transform.cleanit(df)
    df = transform_general.remove_stop_words.remove_stopwords(df, 'Title')
    df = transform_general.remove_stop_words.remove_stopwords(df, 'Text')

    today = date.today()
    fname = "cleaned_news_catcher_" + str(today) + '.csv'

    information.savetoBucket_csv(df, 'newsdata', fname)
    create_Ngram.Ngram(df, 'news_catcher' + str(today), 'Text_without_stopwords')
    create_Ngram.Ngram(df, 'news_catcher' + str(today) ,'Title_without_stopwords')

    df['camefrom'] = 'newsCatcher'

    return df