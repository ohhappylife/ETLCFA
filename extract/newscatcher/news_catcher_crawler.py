from newscatcherapi import NewsCatcherApiClient
import information
from datetime import date
import pandas as pd
from validation_general import generateStatusCode
from config import credential_news_carcher_key, bool_store_newscatcher_raw, s3_news_catcher_raw

def newsCatcher(keyword):
  """
  Collect news articles based on keyword from News Catcher API.
  :param str keyword: keyword to be searched.
  :return: crawled news articles and its information
  :rtype: dataframe
  """
  today = date.today()

  newscatcherapi = NewsCatcherApiClient(credential_news_carcher_key)
  news_articles = newscatcherapi.get_search(q=keyword)
  df = pd.DataFrame.from_dict(news_articles, orient='index').T
  c = generateStatusCode.dataNotCollected(1, df)

  if c == 1:
    df_temp = (pd.concat({i: pd.DataFrame(x) for i, x in df.pop('articles').items()})
             .reset_index(level=1, drop=True)
             .join(df)
             .reset_index(drop=True))

    generateStatusCode.dataNotCollected(3, df_temp)
    generateStatusCode.columnsChanged(3, df_temp)
    if bool_store_newscatcher_raw == True:
      fname = "raw_news_catcher_" + keyword +'_' + str(today) + '.csv'
      information.savetoBucket_csv(df, s3_news_catcher_raw, fname)
    return df_temp
  else:
    return df
