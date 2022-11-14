from newsapi.newsapi_client import NewsApiClient
import information
from datetime import date, timedelta
import pandas as pd
from validation_general import generateStatusCode
from config import credential_news_api_key, bool_store_newsapi_raw, s3_news_api_raw, timedelta


def crawlData(keyword):
  """
  Crawl Nes data from News API based on keyword
  :param string keyword: Keyword to be searched
  :return: collected news articles and its information.
  :rtype: dataframe
  """
  newsapi = NewsApiClient(api_key=credential_news_api_key)

  yesterday = date.today() - timedelta(days=timedelta)
  today = date.today()

  all_articles = newsapi.get_everything(q=keyword,
                                        from_param=yesterday,
                                        to=today,
                                        language='en',
                                        sort_by='relevancy',
                                        page=2)
  all_articles = pd.DataFrame.from_dict(all_articles, orient='index')
  all_articles = all_articles.T

  df_temp = (pd.concat({i: pd.DataFrame(x) for i, x in all_articles.pop('articles').items()})
             .reset_index(level=1, drop=True)
             .join(all_articles)
             .reset_index(drop=True))
  c = generateStatusCode.dataNotCollected(1, df_temp)

  if c == 1:
    normalized = pd.json_normalize(df_temp['source'])
    df_temp = df_temp.join(normalized).drop(columns=['source'])

    generateStatusCode.dataNotCollected(2, df_temp)
    generateStatusCode.columnsChanged(2, df_temp)

    if bool_store_newsapi_raw == True:
        fname = "raw_news_" + keyword + '_' + str(today) + '.csv'
        information.savetoBucket_csv(df_temp, s3_news_api_raw, fname)
    return df_temp

  else:
    return df_temp