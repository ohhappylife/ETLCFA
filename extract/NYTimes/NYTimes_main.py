from datetime import date
import information
from extract.NYTimes import NYTimesCrawler, NYTimes_transform
from transform_general import create_Ngram, remove_stop_words

def crawlit(keyword):
  df = NYTimesCrawler.runit(keyword)
  if len(df) == 0:
    pass
  else:
    df = NYTimes_transform.cleanit(df)
    df = remove_stop_words.remove_stopwords(df)

    today = date.today()
    fname = "cleaned_NYTimes_" + str(today) + '.csv'

    information.savetoBucket(df, 'newsdata', fname)
    create_Ngram.Ngram(df, 'NYTimes_Ngram' + str(today))
    df['camefrom'] = 'NYTimes'

    return df
