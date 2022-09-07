from newsapi import NewsApiClient
import information
from datetime import date, timedelta
import pandas as pd

def crawlData(keyword):
  newsapi = NewsApiClient(api_key=information.news())

  yesterday = date.today() - timedelta(days=2)
  today = date.today()

  all_articles = newsapi.get_everything(q=keyword,
                                        from_param=yesterday,
                                        to=today,
                                        language='en',
                                        sort_by='relevancy',
                                        page=2)
  all_articles = pd.DataFrame.from_dict(all_articles, orient='index')
  all_articles = all_articles.T

  df_temp = (pd.concat({i: pd.DataFrame(x) for i, x in all_articles.pop('articles').items()})
             .reset_index(level=1, drop=True)
             .join(all_articles)
             .reset_index(drop=True))

  normalized = pd.json_normalize(df_temp['source'])
  df_temp = df_temp.join(normalized).drop(columns=['source'])

  fname = "raw_news" + str(today) + '.csv'
  information.savetoBucket(df_temp, 'newsdata', fname)

  df = pd.DataFrame(
    columns=['Author', 'Published Date', 'Title', 'Text', 'Title_without_stopwords', 'Text_without_stopwords',
             'Language', 'Site_url', 'Main_img_url', 'Type', 'Label', 'hasImage'])
  df['Author'] = df_temp['source']
  df['Published Date'] = df_temp['pub_date'].astype(str).str.split(' ').str[0]
  df['Title'] = df_temp['headline.main']
  df['Text'] = df_temp['abstract']
  df['Title_without_stopwords'] = ''
  df['Text_without_stopwords'] = ''
  df['Language'] = 'English'
  df['Site_url'] = df_temp['web_url']
  df['Main_img_url'] = False
  df['Type'] = 'Unknown'
  df['Label'] = 'Unknown'
  df['hasImage'] = df_temp['urlToImage'].notnull()

  # Show the data set
  today = date.today()
  fname = "uncleared_news_" + str(today) + '.csv'
  information.savetoBucket(df_temp, 'newsdata', fname)

  return df
