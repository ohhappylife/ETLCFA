from datetime import date
import store_to_s3
import transform_general.remove_stop_words
from extract.googleNews import google_crawler, google_transform
from Analyze_General import create_Ngram
from config import bool_store_google_clean, bool_store_google_ngram

def googleNews(keyword):
  """
  collect news from Google based on a keyword and clean it.
  :param str keyword: collected news articles and transform articles based on keyword.
  :return: cleaned news articles
  :rtype: dataframe
  """
  df = google_crawler.crawlData(keyword)
  if len(df)==0:
    pass
  else:
    df = google_transform.cleanIT(df, keyword)
    df = google_transform.changeDateType(df)
    df = transform_general.remove_stop_words.remove_stopwords(df, 'Title')
    df = transform_general.remove_stop_words.remove_stopwords(df, 'Text')
    today = date.today()
    fname = "cleaned_google_" +keyword + '_' + str(today) + '.csv'
    if bool_store_google_clean == True:
      store_to_s3.savetoBucket_csv(df, 'newscleanedgooglenews', fname)
    if bool_store_google_ngram == True:
      create_Ngram.Ngram(df, 'google_Ngram' + keyword + '_' + str(today), 'Text_without_stopwords')
      create_Ngram.Ngram(df, 'google_Ngram' + keyword + '_' + str(today), 'Title_without_stopwords')

    df['camefrom'] = 'GoogleNews'

    return df