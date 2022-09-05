from datetime import date

import information
import transform_general.remove_stop_words
from googleNews import google_transform, google_crawler
from transform_general import save_csv_file, create_Ngram

def googleNews(keyword):
  df = google_crawler.crawlData(keyword)
  df = google_transform.changeDateType(df)
  df = transform_general.remove_stop_words.remove_stopwords(df)

  today = date.today()
  fname = "cleaned_google_" + str(today) + '.csv'

  information.savetoBucket(df, 'newsdata', fname)
  create_Ngram.Ngram(df, 'google_Ngram' + str(today))