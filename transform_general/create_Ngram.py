import pandas as pd
import save_csv_file
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
    ftitle = name + "_title_" + '_' + str(i)
    fvalue = name + "_text_" + '_' + str(i)

    ngram_title = (pd.Series(nltk.ngrams(title, i)).value_counts()).reset_index()
    ngram_value = (pd.Series(nltk.ngrams(text, i)).value_counts()).reset_index()
    save_csv_file.save_file(ngram_title, ftitle)
    save_csv_file.save_file(ngram_value, fvalue)


