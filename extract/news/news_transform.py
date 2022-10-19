import information
from datetime import date
import pandas as pd

def cleanit(df_temp, keyword):
  """
  Clean the news articles that are collected from News API.
  :param dataframe df_temp: dataframe that is collected from crawler.
  :return: Cleaned articles and its information.
  :rtype: dataframe
  """
  df = pd.DataFrame(
    columns=['Author', 'Published Date', 'Title', 'Text', 'Title_without_stopwords', 'Text_without_stopwords',
             'Language', 'Site_url', 'Main_img_url', 'Type', 'Label', 'hasImage'])
  df['Author'] = df_temp['name']
  df['Published Date'] = df_temp['publishedAt'].str[:10]
  df['Title'] = df_temp['title']
  df['Text'] = df_temp['content']
  df['Title_without_stopwords'] = ''
  df['Text_without_stopwords'] = ''
  df['Language'] = 'English'
  df['Site_url'] = df_temp['url']
  df['Main_img_url'] = df_temp['urlToImage']
  df['Type'] = 'Unknown'
  df['Label'] = 'Unknown'
  df['hasImage'] = df_temp['urlToImage'].notnull()

  # Show the data set
  today = date.today()
  fname = "uncleared_news_"  + keyword + '_' + str(today) + '.csv'
  information.savetoBucket_csv(df_temp, 'newsdata', fname)

  return df