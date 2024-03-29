from Load import store_to_s3
from extract.bingNews import bing_Crawler, bing_Transform
from transform_general import remove_stop_words, resolve_encoding_issues
from Analyze_General import create_Ngram
from datetime import date
from config import s3_bing_news_cleaned, bool_store_bing_clean, bool_store_bing_ngram

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
    df = bing_Transform.cleanIT(df, keyword)
    df = resolve_encoding_issues.HTMLtoChar(df, 'Title')
    df = resolve_encoding_issues.HTMLtoChar(df, 'Text')

    df = remove_stop_words.remove_stopwords(df, 'Title')
    df = remove_stop_words.remove_stopwords(df, 'Text')

    today = date.today()
    fname = "cleaned_bing_" + keyword + '_' + str(today) + '.csv'
    if bool_store_bing_clean == True:
      store_to_s3.savetoBucket_csv(df, s3_bing_news_cleaned, fname)
    if bool_store_bing_ngram == True:
      create_Ngram.Ngram(df, 'bing_Ngram_' + keyword + '_' + str(today), 'Title_without_stopwords')
      create_Ngram.Ngram(df, 'bing_Ngram' + keyword + '_' + str(today), 'Text_without_stopwords')

    df['camefrom'] = 'BingNews'

    return df