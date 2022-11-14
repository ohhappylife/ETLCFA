from datetime import date
from serpapi import GoogleSearch
import pandas as pd
from validation_general import generateStatusCode
from config import credential_google_key, bool_store_google_raw, s3_google_news_raw
import information

def crawlData(keyword):
    """
    Collect news articels from Google News based on keyword.
    :param str keyword: keyword to be searched from Google News.
    :return: imported file
    :rtype: dataframe
    """
    today = date.today()

    params = {
        "api_key": credential_google_key, # Please user your own API Key.
        "engine": "google",
        "q": keyword,     # keywords to be searched (Required)
        "gl": "us",
        "tbm": "nws"
    }

    search = GoogleSearch(params)   # where data extraction happens on the backend
    results = search.get_dict()     # JSON - > Python dictionary
    result = results["news_results"] # get news information only.

    df_temp = pd.DataFrame(result)

    c = generateStatusCode.dataNotCollected(1, df_temp)
    if c == 1:
        generateStatusCode.columnsChanged(1, df_temp)
        if bool_store_google_raw == True:
            fname = "raw_google_" + keyword + '_' + str(today) + '.csv'
            information.savetoBucket_csv(df_temp, s3_google_news_raw, fname)
        return df_temp

    else:
        return df_temp