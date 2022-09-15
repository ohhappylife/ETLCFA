from newscatcherapi import NewsCatcherApiClient
import information
from datetime import date
import pandas as pd
from validation_general import generateStatusCode

def newsCatcher(keyword):
  """
  Collect news articles based on keyword from News Catcher API.
  :param str keyword: keyword to be searched.
  :return: crawled news articles and its information
  :rtype: dataframe
  """
  today = date.today()

  newscatcherapi = NewsCatcherApiClient(information.catcher())
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

    fname = "raw_news_catcher" + str(today) + '.csv'
    information.savetoBucket(df, 'newsdata', fname)
    return df_temp
  else:
    return df
