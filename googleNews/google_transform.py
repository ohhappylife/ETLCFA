from datetime import datetime, timedelta

from transform_general import remove_stop_words

now = datetime.now()

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

def remove_stopwords(df):
  df = remove_stop_words.remove_stopwords(df)
  return df