"""
  politifact_main.py
  crawl the data from politifact, clean the datasets and store the datasets.
    requirements : Users shall have privileges to save the file into a cwd.
    input : none
    output : four folders, 8 csv files
"""
__author__ = "Shon"
__version__ = "1.0.1"
__email__ = "sshon2@alumni.jh.edu"
__status__ = "Production"

from datetime import date

import information
from extract.politifact import politifact_crawler, politifact_transofrm
from transform_general import create_Ngram, remove_stop_words


def crawlit():
  df = politifact_crawler.runit()
  if len(df) == 0:
    pass
  else:
    df = politifact_transofrm.transofmr_politifact(df)
    df = remove_stop_words.remove_stopwords(df, 'Title')
    df = remove_stop_words.remove_stopwords(df, 'Text')

    today = date.today()
    fname = "cleaned_politifact_" + str(today) + '.csv'

    information.savetoBucket(df, 'newsdata', fname)

    create_Ngram.Ngram(df, 'politifact_Ngram' + str(today), 'Title_without_stopwords')
    create_Ngram.Ngram(df, 'politifact_Ngram' + str(today), 'Text_without_stopwords')

    df['camefrom'] = 'politifact'
    return df
