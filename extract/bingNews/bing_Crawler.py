import requests
import json
from datetime import date
import information
import pandas as pd
from validation_general import generateStatusCode

today = date.today()

def crawlIt(keyword):
  subscription_key = information.Bing()
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
    fname = "raw_bing" + str(today) + '.csv'
    information.savetoBucket(df_temp, 'newsdata', fname)
    return df_temp

  else:
    return df_temp