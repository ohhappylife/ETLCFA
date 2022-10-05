from extract.news import news_transform, news_crawler
from transform_general import remove_stop_words, create_Ngram
from datetime import date
import information

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
    df = news_transform.cleanit(df)
    df = remove_stop_words.remove_stopwords(df, 'Title')
    df = remove_stop_words.remove_stopwords(df, 'Text')

    today = date.today()
    fname = "cleaned_news" + str(today) + '.csv'

    information.savetoBucket_csv(df, 'newsdata', fname)
    create_Ngram.Ngram(df, 'news' + str(today), 'Text_without_stopwords')
    create_Ngram.Ngram(df, 'news' + str(today) ,'Title_without_stopwords')

    df['camefrom'] = 'newsAPI'

    return df