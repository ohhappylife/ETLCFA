from datetime import date

import store_to_s3
from extract.NYTimes import NYTimesCrawler, NYTimes_transform
from transform_general import remove_stop_words
from Analyze_General import create_Ngram
from config import bool_store_nytimesapi_clean, bool_store_nytimesapi_ngram


def crawlit(keyword):
  """
  collect news from Bing based on a keyword and clean it.
  :param str keyword: collected news articles and transform articles based on keyword.
  :return: cleaned news articles
  :rtype: dataframe
  """
  df = NYTimesCrawler.runit(keyword)
  if len(df) == 0:
    pass
  else:
    df = NYTimes_transform.cleanit(df, keyword)
    df = remove_stop_words.remove_stopwords(df, 'Title')
    df = remove_stop_words.remove_stopwords(df, 'Text')

    today = date.today()
    if bool_store_nytimesapi_clean == True:
      fname = "cleaned_NYTimes_" + keyword + '_' + str(today) + '.csv'
      store_to_s3.savetoBucket_csv(df, 'newscleanednytimes', fname)

    if bool_store_nytimesapi_ngram == True:
      create_Ngram.Ngram(df, 'NYTimes_Ngram_' + keyword + '_' + str(today), 'Text_without_stopwords')
      create_Ngram.Ngram(df, 'NYTimes_Ngram_' + keyword + '_' + str(today), 'Title_without_stopwords')

    df['camefrom'] = 'NYTimes'

    return df
