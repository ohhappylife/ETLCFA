from newscatcherapi import NewsCatcherApiClient
import information
from datetime import date
import pandas as pd

def newsCatcher(keyword):
  newscatcherapi = NewsCatcherApiClient(information.catcher())
  news_articles = newscatcherapi.get_search(q=keyword)
  df = pd.DataFrame.from_dict(news_articles, orient='index').T
  df_temp = (pd.concat({i: pd.DataFrame(x) for i, x in df.pop('articles').items()})
           .reset_index(level=1, drop=True)
           .join(df)
           .reset_index(drop=True))

  df = pd.DataFrame(
    columns=['Author', 'Published Date', 'Title', 'Text', 'Title_without_stopwords', 'Text_without_stopwords',
             'Language', 'Site_url', 'Main_img_url', 'Type', 'Label', 'hasImage'])
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
  df['hasImage'] = 'Unknwon'

  # Show the data set
  today = date.today()
  fname = "uncleared_news_catcher" + str(today) + '.csv'
  information.savetoBucket(df, 'newsdata', fname)

  return df