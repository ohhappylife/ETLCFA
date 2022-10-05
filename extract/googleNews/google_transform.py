from datetime import datetime, timedelta
from transform_general import remove_stop_words
from datetime import date
import pandas as pd
import information

now = datetime.now()

def cleanIT(df_temp):
  """
  Clean collected news articles from google_crawler.py
  :param dataframe df_temp: collected news article and it's information from google_crawler.py
  :return: clean news article and its information
  :rtype: dataframe
  """
  df = pd.DataFrame(
    columns=['Author', 'Published Date', 'Title', 'Text', 'Title_without_stopwords', 'Text_without_stopwords',
             'Language', 'Site_url', 'Main_img_url', 'Type', 'Label', 'hasImage'])
  df['Author'] = df_temp['source']
  df['Published Date'] = df_temp['date']
  df['Title'] = df_temp['title']
  df['Text'] = df_temp['snippet']
  df['Title_without_stopwords'] = ''
  df['Text_without_stopwords'] = ''
  df['Language'] = 'English'
  df['Site_url'] = df_temp['link']
  df['Main_img_url'] = df_temp['thumbnail']
  df['Type'] = 'Unknown'
  df['Label'] = 'Unknown'
  df['hasImage'] = df_temp['thumbnail'].notnull()

  # Show the data set
  today = date.today()
  fname = "uncleared_google_" + str(today) + '.csv'
  information.savetoBucket_csv(df, 'newsdata', fname)
  return df

def hour(hour):
    mod_date = now + timedelta(hours = -hour)
    mod_date = str(mod_date.year) + '-' + str(mod_date.month) + '-' + str(mod_date.hour)
    return mod_date

def day(day):
    mod_date = now + timedelta(days = -day)
    mod_date = str(mod_date.year) + '-' + str(mod_date.month) + '-' + str(mod_date.hour)
    return mod_date

def month(month):
    mod_date = now + timedelta(months = -month)
    mod_date = str(mod_date.year) + '-' + str(mod_date.month) + '-' + str(mod_date.hour)
    return mod_date

def changeDateType(df):
  for index, row in df.iterrows():
    if row['Published Date'].split(' ')[1] in (['day' , 'days']):
      t = int(row['Published Date'].split(' ')[0])
      df.iloc[index, df.columns.get_loc('Published Date')] = day(t)
    elif row['Published Date'].split(' ')[1] in (['hour' , 'hours']):
      t = int(row['Published Date'].split(' ')[0])
      df.iloc[index, df.columns.get_loc('Published Date')] = hour(t)
    elif row['Published Date'].split(' ')[1] in (['month' , 'months']):
      t = int(row['Published Date'].split(' ')[0])
      df.iloc[index, df.columns.get_loc('Published Date')] = month(t)
  return df