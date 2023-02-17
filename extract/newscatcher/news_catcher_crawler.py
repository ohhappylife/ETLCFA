from newscatcherapi import NewsCatcherApiClient
from datetime import date
import pandas as pd
from Load import store_to_s3
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
  if str(df['status'])[0:32].replace(" ","")!=("0Nomatchesforyoursearch."):
    if c == 1 and str(df.pop('status')) != "No matches for your search.":
      df_temp = (pd.concat({i: pd.DataFrame(x) for i, x in df.pop('articles').items()})
               .reset_index(level=1, drop=True)
               .join(df)
               .reset_index(drop=True))

      generateStatusCode.dataNotCollected(3, df_temp)
      generateStatusCode.columnsChanged(3, df_temp)
      if bool_store_newscatcher_raw == True:
        fname = "raw_news_catcher_" + keyword +'_' + str(today) + '.csv'
        store_to_s3.savetoBucket_csv(df, s3_news_catcher_raw, fname)
      return df_temp
    else:
      return df
  else:
    return pd.DataFrame(columns=['Author', 'Published Date', 'Title', 'Text', 'Title_without_stopwords', 'Text_without_stopwords',
                                   'Language', 'Site_url', 'Main_img_url', 'Type','Label', 'hasImage'])