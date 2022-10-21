from datetime import datetime, timedelta
import pandas as pd
from datetime import date
import information


now = datetime.now()

def cleanIT(df_temp,keyword):
  """
  Clean news articles that are collected from bing_Crawler.py
  :param dataframe df_temp: collected news articles and it's information.
  :return: cleaned news articles
  :rtype: dataframe
  """
  df = pd.DataFrame(
    columns=['Author', 'Published Date', 'Title', 'Text', 'Title_without_stopwords', 'Text_without_stopwords',
             'Language', 'Site_url', 'Main_img_url', 'Type', 'Label', 'hasImage'])
  df['Author'] = df_temp['provider'].astype(str).str.split(",").str[1].astype(str).str.split(" on ").str[0].str.replace('\'', "").str.replace('name: ', "")
  df['Published Date'] = df_temp['datePublished'].str.split("T").str[0]
  df['Title'] = df_temp['name'].str.replace('<b>', "").str.replace('</b>', "")
  df['Text'] = df_temp['description']
  df['Title_without_stopwords'] = ''
  df['Text_without_stopwords'] = ''
  df['Language'] = 'English'
  df['Site_url'] = df_temp['url']
  df['Main_img_url'] = df_temp['image.thumbnail.contentUrl']
  df['Type'] = 'Unknown'
  df['Label'] = 'Unknown'
  df['hasImage'] = df_temp['image.thumbnail.contentUrl'].notnull()

  today = date.today()
#  fname = "uncleared_bingNews_" + keyword + '_' + str(today) + '.csv'
#  information.savetoBucket_csv(df, 'newscleanedbingnews', fname)
  return df