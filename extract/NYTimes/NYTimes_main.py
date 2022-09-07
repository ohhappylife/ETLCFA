from datetime import date

import information
from extract.NYTimes import NYTimesCrawler
from transform_general import create_Ngram

def crawlit():
  df = NYTimesCrawler.runit()

  today = date.today()
  fname = "cleaned_NYTimes_" + str(today) + '.csv'

  information.savetoBucket(df, 'newsdata', fname)

  create_Ngram.Ngram(df, 'NYTimes_Ngram' + str(today))

crawlit()