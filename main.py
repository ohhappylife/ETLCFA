import sys
from extract.newscatcher import news_catcher_main
from extract.googleNews import google_main
from extract.politifact import politifact_main
from extract.news import news_main
from extract.NYTimes import NYTimes_main
from logger import logger
from extract.bingNews import bing_main
import pandas as pd
from datetime import date
from transform_general import resolve_encoding_issues
import information
from Analyze_General import extract_keyword, summraize_text
from config import s3_news_merged, bool_store_merged_csv, bool_store_merged_excel, bool_extract_keyworde, \
    bool_text_extract, bool_get_politifact, bool_get_google, bool_get_newsCatcher,bool_get_bing, bool_get_newsApi, bool_get_nytimes
from validation_general import checkSize

logger.debug("start the process")

try:
    keyword = sys.argv[1]  # To test at the Pycharm. Please change it into 0 after the testing.
    logger.debug("Received Keyword : " + str(keyword))
except IndexError:
    logger.critical("err 001: No keyword is given")
    exit(-1)

df = pd.DataFrame(columns=['Author', 'Published Date', 'Title', 'Text', 'Title_without_stopwords', 'Text_without_stopwords',
                           'Language', 'Site_url', 'Main_img_url', 'Type','Label', 'hasImage'])
if bool_get_bing==True:
    dfb = bing_main.bingNews(keyword)
    df = pd.concat([df, dfb])
    logger.debug('Crawl Bing news')
if bool_get_newsCatcher==True:
    dfnc = news_catcher_main.newsCatcher(keyword)
    df = pd.concat([df, dfnc])
    logger.debug("Crawl News Catcher")
if bool_get_google==True:
    dfg = google_main.googleNews(keyword)
    df = pd.concat([df, dfg])
    logger.debug("Crawl Google News")
if bool_get_politifact==True:  # Politifact does not support keyword search.
    dfp = politifact_main.crawlit(keyword)
    df = pd.concat([df, dfp])
    logger.debug("Crawl Poltifiact")
if bool_get_newsApi==True:
    dfn = news_main.news(keyword)
    df = pd.concat([df, dfn])
    logger.debug("Crawl News API")
if bool_get_nytimes==True:
    dfny = NYTimes_main.crawlit(keyword)
    df = pd.concat([df, dfny])
    logger.debug("Crawl NYTimes")
if(bool_get_bing==False & bool_get_newsCatcher==False & bool_get_google==False
        & bool_get_politifact==False & bool_get_newsApi==False & bool_get_nytimes==False):
    exit(-1)

if checkSize.checkrow(df) > 0:
    today = date.today()
    df = resolve_encoding_issues.resolveEncodeIssue(df)  # resolve some encode issues; temporary method
    df = df.reset_index(drop=True)
    df = df.drop(columns=['Unnamed: 0'])
    df.dropna(subset=['Author'], inplace=True)

    if bool_extract_keyworde==True:
        df = extract_keyword.get_keyword(df)
    if bool_text_extract==True:
        df = summraize_text.summarize(df)
    if bool_store_merged_csv==True:
        fname_csv = "merged_" + keyword + '_' + str(today) + '.csv'
    if bool_store_merged_excel==True:
        fname_excel = "merged_" + keyword + '_' + str(today) + '.xlsx'
    if bool_store_merged_csv == True:
        information.savetoBucket_csv(df, s3_news_merged, fname_csv)
    if bool_store_merged_excel == True:
        information.savetoBucket_excel(df, s3_news_merged , fname_excel)

else:
    logger.error("no data collected")
logger.debug("end the process")
