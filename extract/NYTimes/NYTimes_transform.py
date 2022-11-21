import information
from datetime import date
import pandas as pd

import store_to_s3
from config import bool_store_nytimesapi_unclean, s3_ny_times_uncleaned

def cleanit(df_temp, keyword):
  """
   Clean the news articles that are collected from NY times API.
   :param dataframe df_temp: dataframe that is collected from crawler.
   :return: Cleaned articles and its information.
   :rtype: dataframe
   """
  df = pd.DataFrame(columns=['Author', 'Published Date', 'Title', 'Text',
                             'Title_without_stopwords', 'Text_without_stopwords',
                             'Language', 'Site_url', 'Main_img_url', 'Type',
                             'Label', 'hasImage'])
  df['Author'] = df_temp['source']
  df['Published Date'] = df_temp['pub_date'].astype(str).str.split().str[0]
  df['Title'] = df_temp['headline.main']
  df['Text'] = df_temp['abstract']
  df['Title_without_stopwords'] = ''
  df['Text_without_stopwords'] = ''
  df['Language'] = 'English'
  df['Site_url'] = df_temp['web_url']
  df['Main_img_url'] = ''
  df['Type'] = 'Unknown'
  df['Label'] = 'Unknown'
  df['hasImage'] = False

  # Show the data set
  if bool_store_nytimesapi_unclean == True:
    today = date.today()
    fname = "uncleared_NYTimes_" + keyword + '_' + str(today) + '.csv'
    store_to_s3.savetoBucket_csv(df, s3_ny_times_uncleaned, fname)

  return df