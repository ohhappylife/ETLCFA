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

  df = pd.DataFrame(columns=['Author', 'Published Date', 'Title', 'Text',
                             'Title_without_stopwords', 'Text_without_stopwords',
                             'Language', 'Site_url', 'Main_img_url', 'Type',
                             'Label', 'hasImage'])
  df['Author'] = df_temp['author']
  df['Published Date'] = df_temp['published_date'].str.split().str[0]
  df['Title'] = df_temp['title']
  df['Text'] = df_temp['summary']
  df['Title_without_stopwords'] = ''
  df['Text_without_stopwords'] = ''
  df['Language'] = 'English'
  df['Site_url'] = df_temp['link']
  df['Main_img_url'] = ''
  df['Type'] = 'Unknown'
  df['Label'] = 'Unknown'
  df['hasImage'] = 'Unknown'

  # Show the data set
  fname = "uncleared_NYTimes" + str(today) + '.csv'
  information.savetoBucket(df, 'NYTimes', fname)

  return df