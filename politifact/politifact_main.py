from datetime import date

import politifact_transofrm
import os
import pandas as pd
from transform_general import save_csv_file, create_Ngram

os.system('python politifact_crawler.py')
today = date.today()

wdir = "politifact_" + str(today) + ".csv/" + "politifact_" + str(today) + ".csv"
df = pd.read_csv(wdir)
df = politifact_transofrm.transofmr_politifact(df)

today = date.today()
fname = "cleaned_politifact_" + str(today)
save_csv_file.save_file(df, fname)

create_Ngram.Ngram(df, "politifact")