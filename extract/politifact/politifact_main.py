"""
  politifact_main.py
  crawl the data from politifact, clean the datasets and store the datasets.
    requirements : Users shall have privileges to save the file into a cwd.
"""
__author__ = "Shon"
__version__ = "1.0.1"
__email__ = "sshon2@alumni.jh.edu"
__status__ = "Production"

from datetime import date
from Load import store_to_s3
from extract.politifact import politifact_crawler, politifact_transofrm
from transform_general import remove_stop_words
from Analyze_General import create_Ngram
from config import bool_store_politifact_ngram, s3_poltifiact_cleaned, bool_store_politifact_clean
def crawlit(keyword):
  """
  collect news from Politifact and clean it.
  :param: None
  :return: cleaned news articles
  :rtype: dataframe
  """
  df = politifact_crawler.runit(keyword)
  if len(df) == 0:
    pass
  else:
    df = politifact_transofrm.transofmr_politifact(df)
    df = remove_stop_words.remove_stopwords(df, 'Title')
    df = remove_stop_words.remove_stopwords(df, 'Text')

    today = date.today()
    fname = "cleaned_politifact_" + keyword + '_' + str(today) + '.csv'

    if bool_store_politifact_clean == True:
      store_to_s3.savetoBucket_csv(df, s3_poltifiact_cleaned, fname)

    if bool_store_politifact_ngram == True:
      create_Ngram.Ngram(df, 'politifact_Ngram_' + keyword + str(today), 'Title_without_stopwords')
      create_Ngram.Ngram(df, 'politifact_Ngram_' + keyword + str(today), 'Text_without_stopwords')

    df['camefrom'] = 'politifact'
    return df
