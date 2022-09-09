from newsapi import NewsApiClient
import information
from datetime import date, timedelta
import pandas as pd

def cleanit(df_temp):
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
  df['hasImage'] = False

  # Show the data set
  today = date.today()
  fname = "uncleared_news_catcher" + str(today) + '.csv'
  information.savetoBucket(df, 'newsdata', fname)
  return df