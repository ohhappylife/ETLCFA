from newsapi import NewsApiClient
import temp
from datetime import date, timedelta
import pandas as pd

def crawlData(keyword):
  newsapi = NewsApiClient(api_key=temp.news())

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
  fname = "uncleared_news_" + str(today) + '.csv'
  temp.savetoBucket(df_temp, 'newsdata', fname)

  return df