from datetime import date, timedelta, datetime
from pynytimes import NYTAPI
import information
import pandas as pd

def runit(keyword, n = 50):
  nyt = NYTAPI(information.NYTimes(), parse_dates=True)

  yesterday = date.today() - timedelta(days=2)
  today = date.today()

  articles = nyt.article_search(
    query=keyword,
    results=n,
    dates={
      "begin": datetime(int(yesterday.year), int(yesterday.month), int(yesterday.day)),
      "end": datetime(int(today.year), int(today.month), int(today.day))
    },
    options={
      "sort": "oldest",
    }
  )

  df_temp = pd.json_normalize(articles)
  fname = "RAW_NYTimes" + str(today) + '.csv'
  information.savetoBucket(df_temp, 'newsdata', fname)

  return df_temp