"""
  tokenize_words.py
  get sentence and return tokenized sentences
"""

from nltk.tokenize import word_tokenize

def tokenize_words(df, col_name):
  """
  Tokenize news articles for analysis.
  :param dataframe df: dataframe to be cleaned.
  :return: dataframe with tokenized article
  :rtype: dataframe
  """
  col = col_name + 'tokenized'
  df[col] = df[col_name].apply(word_tokenize)
  return df