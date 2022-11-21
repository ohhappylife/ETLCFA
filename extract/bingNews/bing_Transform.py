from datetime import datetime
import pandas as pd
from datetime import date

import store_to_s3
from config import s3_bing_news_uncleaned, bool_store_bing_unclean

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
  if bool_store_bing_unclean == True:
    fname = "uncleared_bingNews_" + keyword + '_' + str(today) + '.csv'
    store_to_s3.savetoBucket_csv(df, s3_bing_news_uncleaned, fname)
  return df