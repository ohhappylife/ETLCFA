from datetime import date
import information
from extract.NYTimes import NYTimesCrawler, NYTimes_transform
from transform_general import create_Ngram, remove_stop_words

def crawlit(keyword):
  """
  collect news from Bing based on a keyword and clean it.
  :param str keyword: collected news articles and transform articles based on keyword.
  :return: cleaned news articles
  :rtype: dataframe
  """
  df = NYTimesCrawler.runit(keyword, 1000)
  if len(df) == 0:
    pass
  else:
    df = NYTimes_transform.cleanit(df)
    df = remove_stop_words.remove_stopwords(df, 'Title')
    df = remove_stop_words.remove_stopwords(df, 'Text')

    today = date.today()
    fname = "cleaned_NYTimes_" + str(today) + '.csv'

    information.savetoBucket_csv(df, 'newsdata', fname)
    create_Ngram.Ngram(df, 'NYTimes_Ngram' + str(today), 'Text_without_stopwords')
    create_Ngram.Ngram(df, 'NYTimes_Ngram' + str(today), 'Title_without_stopwords')

    df['camefrom'] = 'NYTimes'

    return df
