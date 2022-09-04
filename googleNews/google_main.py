from datetime import date
import os
import pandas as pd

import transform_general.remove_stop_words
from googleNews import google_transform
from transform_general import save_csv_file, create_Ngram
from google_crawler import crawlData

def googleNews(keyword):
  today = date.today()

  df = crawlData(keyword)
  df = google_transform.changeDateType(df)
  df = transform_general.remove_stop_words.remove_stopwords(df)

  today = date.today()
  fname = "cleaned_google" + str(today)
  save_csv_file.save_file(df, 'google_cleared',fname)

  create_Ngram.Ngram(df, 'google_Ngram')
