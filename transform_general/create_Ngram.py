"""
  create_Ngram.py
  Generating N-gram from sentences
    requirements : dataframe shall have columns of Title_without_stopwords columns and Text_without_stopwords columns
    input : dataframe Title_without_stopwords columns and Text_without_stopwords columns
    output : unigram, bigram, trigram of input
  To change the N-gram (e.g., to quadgram), chane the range in for-loop.
"""
__author__ = "Shon"
__version__ = "1.0.1"
__email__ = "sshon2@alumni.jh.edu"
__status__ = "Production"

import pandas as pd
import information
import re
import unicodedata
import nltk

def basic_clean(text):
  wnl = nltk.stem.WordNetLemmatizer()
  text = (unicodedata.normalize('NFKD', text)
    .encode('ascii', 'ignore')
    .decode('utf-8', 'ignore')
    .lower())
  words = re.sub(r'[^\w\s]', '', text).split()
  return [wnl.lemmatize(word) for word in words]

def Ngram(df, name):
  title = basic_clean(''.join(str(df['Title_without_stopwords'].tolist())))
  text = basic_clean(''.join(str(df['Text_without_stopwords'].tolist())))

  for i in range(1,4):
    ftitle = name + "_title_" + '_' + str(i) + '.csv'
    fvalue = name + "_text_" + '_' + str(i) + '.csv'

    ngram_title = (pd.Series(nltk.ngrams(title, i)).value_counts()).reset_index()
    ngram_value = (pd.Series(nltk.ngrams(text, i)).value_counts()).reset_index()

    information.savetoBucket(ngram_title, 'ngram', ftitle)
    information.savetoBucket(ngram_value, 'ngram', fvalue)


