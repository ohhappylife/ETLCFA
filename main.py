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
from other_general import credential
from other_general import load_csv_file

logger.debug("start the process")

cr = credential.credential
ls = load_csv_file.readLinebyLine('credential.txt')

cr.s3_bing_news_raw = ls[0]
cr.s3_bing_news_cleaned = ls[1]
cr.s3_google_news_raw = ls[2]
cr.s3_google_news_cleaned = ls[3]
cr.s3_news_api_raw = ls[4]
cr.s3_news_api_cleaned = ls[5]
cr.s3_news_catcher_raw = ls[6]
cr.s3_news_catcher_cleaned = ls[7]
cr.s3_ny_times_raw = ls[8]
cr.s3_ny_times_cleaned = ls[9]
cr.s3_poltifiact_raw = ls[10]
cr.s3_Ngram = ls[11]
cr.cr_google_key = ls[12]
cr.cr_news_catcher_key = ls[13]
cr.cr_news_api_key = ls[14]
cr.cr_NYTimes_key = ls[15]
cr.cr_Bing_key = ls[16]
cr.cr_aws_key = ls[17]
cr.cr_aws_secret = ls[18]

try:
    keyword = sys.argv[1]  # To test at the Pycharm. Please change it into 0 after the testing.
    logger.debug("Received Keyword : " + str(keyword))
except IndexError:
    logger.critical("err 001: No keyword is given")
    exit(-1)

try:
    catcher = sys.argv[2]  # 1
    google = sys.argv[3]  # 2
    politifact = sys.argv[4]  # 3
    news = sys.argv[5]  # 4
    NYTtimes = sys.argv[6]  # 5
    Bing = sys.argv[7]  # 6

    df = pd.DataFrame(columns=['Author', 'Published Date', 'Title', 'Text',
                               'Title_without_stopwords', 'Text_without_stopwords',
                               'Language', 'Site_url', 'Main_img_url', 'Type',
                               'Label', 'hasImage'])

    if catcher != 0:
        dfnc = news_catcher_main.googleNews(keyword)
        df = pd.concat([df, dfnc])
        logger.debug("Crawl News Catcher")
    if google != 0:
        dfg = google_main.googleNews(keyword)
        df = pd.concat([df, dfg])
        logger.debug("Crawl Google News")
    if politifact != 0:  # Politifact does not support keyword search.
        dfp = politifact_main.crawlit(keyword)
        df = pd.concat([df, dfp])
        logger.debug("Crawl Poltifiact")
    if news != 0:
        dfn = news_main.news(keyword)
        df = pd.concat([df, dfn])
        logger.debug("Crawl News API")
    if NYTtimes != 0:
        dfny = NYTimes_main.crawlit(keyword)
        df = pd.concat([df, dfny])
        logger.debug("Crawl NYTimes")
    if Bing != 0:
        dfb = bing_main.bingNews(keyword)
        df = pd.concat([df, dfb])
        logger.debug('Crawl Bing news')

except IndexError:
    logger.debug("Crawl from ALL sources")
    dfp = politifact_main.crawlit(keyword)
    dfnc = news_catcher_main.googleNews(keyword)
    dfg = google_main.googleNews(keyword)
    dfn = news_main.news(keyword)
    dfny = NYTimes_main.crawlit(keyword)
    dfb = bing_main.bingNews(keyword)
    df = pd.concat([dfp, dfnc, dfg, dfn, dfny, dfb])

today = date.today()

df = resolve_encoding_issues.resolveEncodeIssue(df)  # resolve some encode issues; temporary method
df = df.reset_index(drop=True)
df = df.drop(columns=['Unnamed: 0'])
df = extract_keyword.get_keyword(df)
df = summraize_text.summarize(df)
df.dropna(subset=['Author'], inplace=True)
fname_csv = "merged_" + keyword + '_' + str(today) + '.csv'
fname_excel = "merged_" + keyword + '_' + str(today) + '.xlsx'

information.savetoBucket_csv(df, 'newsmergedcleaned', fname_csv)
information.savetoBucket_excel(df, 'newsmergedcleaned', fname_excel)

logger.debug("end the process")
