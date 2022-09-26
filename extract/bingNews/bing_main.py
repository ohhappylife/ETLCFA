from extract.bingNews import bing_Crawler, bing_Transform
from transform_general import remove_stop_words, create_Ngram, resolve_encoding_issues
from datetime import date
import information

def bingNews(keyword):
  """
  collect news from Bing based on a keyword and clean it.
  :param str keyword: collected news articles and transform articles based on keyword.
  :return: cleaned news articles
  :rtype: dataframe
  """
  df = bing_Crawler.crawlIt(keyword)
  if len(df)==0: # no article is collected
    pass
  else: # article is collected
    df = bing_Transform.cleanIT(df)
    df = resolve_encoding_issues.HTMLtoChar(df)
    df = remove_stop_words.remove_stopwords(df, 'Title')
    df = remove_stop_words.remove_stopwords(df, 'Text')

    today = date.today()
    fname = "cleaned_bing_" + str(today) + '.csv'

    information.savetoBucket(df, 'newsdata', fname)
    create_Ngram.Ngram(df, 'bing_Ngram' + str(today), 'Title_without_stopwords')
    create_Ngram.Ngram(df, 'bing_Ngram' + str(today), 'Text_without_stopwords')

    df['camefrom'] = 'BingNews'

    return df