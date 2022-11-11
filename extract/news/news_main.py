from extract.news import news_transform, news_crawler
from transform_general import remove_stop_words, create_Ngram
from datetime import date
import information
from config import bool_store_newsapi_clean, bool_store_newsapi_ngram


def news(keyword):
  """
  collect news from NewsAPI based on a keyword and clean it.
  :param str keyword: collected news articles and transform articles based on keyword.
  :return: cleaned news articles
  :rtype: dataframe
  """
  df = news_crawler.crawlData(keyword)
  if len(df) == 0: # No data is collected
    pass
  else: # Data is collected.
    df = news_transform.cleanit(df, keyword)
    df = remove_stop_words.remove_stopwords(df, 'Title')
    df = remove_stop_words.remove_stopwords(df, 'Text')

    today = date.today()
    fname = "cleaned_news_" +keyword + '_' + str(today) + '.csv'

    if bool_store_newsapi_clean == True:
     information.savetoBucket_csv(df, 'newscleanednewsapi', fname)
    if bool_store_newsapi_ngram == True:
      create_Ngram.Ngram(df, 'news'  + keyword + '_' + str(today), 'Text_without_stopwords')
      create_Ngram.Ngram(df, 'news'  + keyword + '_' + str(today) ,'Title_without_stopwords')

    df['camefrom'] = 'newsAPI'

    return df