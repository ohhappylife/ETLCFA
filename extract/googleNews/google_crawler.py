from datetime import date
from serpapi import GoogleSearch
import pandas as pd
import information
from validation_general import generateStatusCode

def crawlData(keyword):
    """
    Collect news articels from Google News based on keyword.
    :param str keyword: keyword to be searched from Google News.
    :return: imported file
    :rtype: dataframe
    """
    today = date.today()

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

    c = generateStatusCode.dataNotCollected(1, df_temp)
    if c == 1:
        generateStatusCode.columnsChanged(1, df_temp)
        fname = "raw_google_" + keyword + '_' + str(today) + '.csv'
        information.savetoBucket_csv(df_temp, 'newsdata', fname)
        return df_temp

    else:
        return df_temp