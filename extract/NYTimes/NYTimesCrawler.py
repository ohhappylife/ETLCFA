from datetime import date, timedelta, datetime
from pynytimes import NYTAPI
import pandas as pd
import store_to_s3
from validation_general import generateStatusCode
from config import credential_NYTimes_key, bool_store_nytimesapi_raw, s3_ny_times_raw, timediff, maxnumcollected

def runit(keyword):
  """
  Crawl Nes data from NYTimes based on keyword
  :param string keyword: Keyword to be searched
  :return: collected news articles and its information.
  :rtype: dataframe
  """
  nyt = NYTAPI(credential_NYTimes_key, parse_dates=True)

  yesterday = date.today() - timedelta(days=timediff)
  today = date.today()

  articles = nyt.article_search(
    query=keyword,
    results=maxnumcollected,
    dates={
      "begin": datetime(int(yesterday.year), int(yesterday.month), int(yesterday.day)),
      "end": datetime(int(today.year), int(today.month), int(today.day))
    },
    options={
      "sort": "oldest",
    }
  )
  c = generateStatusCode.dataNotCollected(1, articles)

  if c == 1:
    df_temp = pd.json_normalize(articles)
    generateStatusCode.dataNotCollected(5, df_temp)
    generateStatusCode.columnsChanged(5, df_temp)
    if bool_store_nytimesapi_raw == True:
      fname = "raw_NYTimes_" + keyword + '_' + str(today) + '.csv'
      store_to_s3.savetoBucket_csv(df_temp, s3_ny_times_raw, fname)

    return df_temp
  else:
    return articles