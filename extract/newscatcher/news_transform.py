import information
from datetime import date
import pandas as pd
from config import bool_store_newscatcher_unclean, s3_news_catcher_uncleaned

def cleanit(df_temp, keyword):
  """
  Clean the news articles that are collected from Newscatcher API.
  :param dataframe df_temp: dataframe that is collected from crawler.
  :return: Cleaned articles and its information.
  :rtype: dataframe
  """
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
  if bool_store_newscatcher_unclean == True:
    today = date.today()
    fname = "uncleared_news_catcher_" + keyword + '_' + str(today) + '.csv'
    information.savetoBucket_csv(df, s3_news_catcher_uncleaned, fname)
  return df