from datetime import date

import information
import transform_general.remove_stop_words
from extract.googleNews import google_crawler, google_transform
from transform_general import create_Ngram

def googleNews(keyword):
  df = google_crawler.crawlData(keyword)
  if len(df)==0:
    pass
  else:
    df = google_transform.cleanIT(df)
    df = google_transform.changeDateType(df)
    df = transform_general.remove_stop_words.remove_stopwords(df, 'Title')
    df = transform_general.remove_stop_words.remove_stopwords(df, 'Text')

    today = date.today()
    fname = "cleaned_google_" + str(today) + '.csv'

    information.savetoBucket(df, 'newsdata', fname)
    create_Ngram.Ngram(df, 'google_Ngram' + str(today), 'Text_without_stopwords')
    create_Ngram.Ngram(df, 'google_Ngram' + str(today), 'Title_without_stopwords')

    df['camefrom'] = 'GoogleNews'

    return df