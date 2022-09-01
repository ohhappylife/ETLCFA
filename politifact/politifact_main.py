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
import politifact_transofrm
import os
import pandas as pd
from transform_general import save_csv_file, create_Ngram

os.system('python politifact_crawler.py')
today = date.today()

wdir = "politifact_uncleared/" + "politifact_" + str(today) + ".csv"
df = pd.read_csv(wdir)
df = politifact_transofrm.transofmr_politifact(df)

today = date.today()
fname = "cleaned_politifact_" + str(today)
save_csv_file.save_file(df, 'plitifact_cleared',fname)

create_Ngram.Ngram(df, 'politifact_Ngram')