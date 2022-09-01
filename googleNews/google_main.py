from datetime import date
import os
import pandas as pd

from googleNews import google_transform
from transform_general import save_csv_file, create_Ngram

os.system('python google_crawler.py')
today = date.today()

wdir = "google_uncleared/" + "google_" + str(today) + ".csv"
df = pd.read_csv(wdir)
df = google_transform.changeDateType(df)
df = google_transform.remove_stopwords(df)

today = date.today()
fname = "cleaned_google" + str(today)
save_csv_file.save_file(df, 'google_cleared',fname)

create_Ngram.Ngram(df, 'google_Ngram')