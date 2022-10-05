__author__ = "Shon"
__version__ = "1.0.1"
__email__ = "sshon2@alumni.jh.edu"
__status__ = "Development"

import nltk
from nltk.corpus import stopwords

def remove_stopwords(df, col_name):
  """
  Remove stop words from collected news article.
  :param dataframe df: dataframe to be cleaned.
  :return: dataframe with cleaned text.
  :rtype: dataframe
  """
  stop = set(stopwords.words('english'))
  col = col_name + '_without_stopwords'
  df[col] = df.apply(lambda row: nltk.word_tokenize(row[col_name]), axis=1)

  df[col] = df[col].apply(lambda words: [word for word in words if word not in stop])

  df[col] = [' '.join(map(str, l)) for l in df[col]]

  return df
