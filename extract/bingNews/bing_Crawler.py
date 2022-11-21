import requests
import json
from datetime import date
import pandas as pd

import store_to_s3
from validation_general import generateStatusCode
today = date.today()
from config import credential_Bing_key, s3_bing_news_raw, bool_store_bing_raw
def crawlIt(keyword):
  """
  Crawl news articles from Bing News based on keyword.
  :param str keyword: keyword to be searched.
  :return: crawled news articles and its information
  :rtype: dataframe
  """
  subscription_key = credential_Bing_key
  search_url = "https://api.bing.microsoft.com/v7.0/news/search"

  headers = {"Ocp-Apim-Subscription-Key" : subscription_key}
  params  = {"q": keyword, "textDecorations": True, "textFormat": "HTML"}

  response = requests.get(search_url, headers=headers, params=params)
  response.raise_for_status()
  search_results = json.dumps(response.json())

  json_object = json.loads(search_results)

  df_temp = pd.json_normalize(json_object['value'])

  c = generateStatusCode.dataNotCollected(6, df_temp)
  if c == 1:
    generateStatusCode.columnsChanged(6, df_temp)
    if bool_store_bing_raw == True:
      fname = "raw_bing_" + keyword + '_' + str(today) + '.csv'
      store_to_s3.savetoBucket_csv(df_temp, s3_bing_news_raw , fname)
    return df_temp
  else:
    return df_temp