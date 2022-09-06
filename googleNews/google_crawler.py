from datetime import date
from serpapi import GoogleSearch
import pandas as pd
import information

def crawlData(keyword):
    params = {
        "api_key": information.google(), # Please user your own API Key.
        "engine": "google",
        "q": keyword,     # keywords to be searched (Required)
        "gl": "us",
        "tbm": "nws"
    }

    search = GoogleSearch(params)   # where data extraction happens on the backend
    results = search.get_dict()     # JSON - > Python dictionary
    result = results["news_results"] # get news information only.

    df_temp = pd.DataFrame(result)
    df = pd.DataFrame(columns = ['Author', 'Published Date', 'Title', 'Text', 'Title_without_stopwords', 'Text_without_stopwords',
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
    df['Type']  = 'Unknown'
    df['Label'] = 'Unknown'
    df['hasImage'] = "Unknown"

    #Show the data set
    today = date.today()
    fname = "uncleared_google_" + str(today) + '.csv'
    information.savetoBucket(df, 'newsdata', fname)

    return df