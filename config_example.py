# Please change file name into config.py
keyword=["Russia","Ukraine"] #Please add keywords. #Please set the keywords into LIST.
bool_get_politifact=True
bool_get_bing=True
bool_get_google=True
bool_get_newsCatcher=True
bool_get_newsApi=True
bool_get_nytimes =True
bool_store_politifact_raw=True
bool_store_politifact_unclean=True
bool_store_politifact_clean=True
bool_store_politifact_ngram=True
bool_store_bing_raw=True
bool_store_bing_unclean=True
bool_store_bing_clean=True
bool_store_bing_ngram=True
bool_store_google_raw=True
bool_store_google_unclean=True
bool_store_google_clean=True
bool_store_google_ngram=True
bool_store_newscatcher_raw=True
bool_store_newscatcher_unclean=True
bool_store_newscatcher_clean=True
bool_store_newscatcher_ngram=True
bool_store_newsapi_raw=True
bool_store_newsapi_unclean=True
bool_store_newsapi_clean=True
bool_store_newsapi_ngram=True
bool_store_nytimesapi_raw=True
bool_store_nytimesapi_unclean=True
bool_store_nytimesapi_clean=True
bool_store_nytimesapi_ngram=True
bool_store_merged_excel=True
bool_store_merged_csv=True
bool_extract_keyworde=False # temporary disabled; has an issue with a key
bool_text_extract=False # temporary disabled; has an issue with a key
s3_bing_news_raw=""
s3_bing_news_uncleaned=""
s3_bing_news_cleaned=""
s3_bing_news_Ngram=""
s3_google_news_raw=""
s3_google_news_uncleaned=""
s3_google_news_cleaned=""
s3_google_news_Ngram=""
s3_news_api_raw=""
s3_news_api_uncleaned=""
s3_news_api_cleaned=""
s3_news_api_Ngram=""
s3_news_catcher_raw=""
s3_news_catcher_cleaned=""
s3_news_catcher_uncleaned = ""
s3_news_catcher_ngram=""
s3_ny_times_raw=""
s3_ny_times_cleaned=""
s3_ny_times_uncleaned=""
s3_ny_times_ngram=""
s3_poltifiact_raw=""
s3_poltifiact_cleaned=""
s3_politifact_uncleaned=""
s3_politifact_ngram=""
s3_news_merged=""
credential_google_key=""
credential_news_carcher_key=""
credential_news_api_key=""
credential_NYTimes_key=""
credential_Bing_key=""
credential_aws_key=""
credential_aws_secret=""
s3_ngram = ""
loglevel="ERROR"
timediff=2
maxnumcollected=1000
ngram_start=3
ngram_ends=3
summary_min_length=30
summary_max_length=1500
#summary_model="bart-large-cnn" #t5-base or bart-large-cnn