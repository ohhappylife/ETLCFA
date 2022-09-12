from extract.bingNews import bing_Crawler, bing_Transform
from transform_general import remove_stop_words, create_Ngram
from datetime import date
import information

def bingNews(keyword):
  df = bing_Crawler.crawlIt(keyword)
  if len(df)==0: # no article is collected
    pass
  else: # article is collected
    df = bing_Transform.cleanIT(df)
    df = remove_stop_words.remove_stopwords(df)

    today = date.today()
    fname = "cleaned_bing_" + str(today) + '.csv'

    information.savetoBucket(df, 'newsdata', fname)
    create_Ngram.Ngram(df, 'bing_Ngram' + str(today))
    df['camefrom'] = 'BingNews'

    return df