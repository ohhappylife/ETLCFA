"""
  tokenize_words.py
  tokenize Title_without_stopwords and Text_without_stopwords columns
    requirements : Title_without_stopwords and Text_without_stopwords columns shall be existed.
    input : dataframe
    output : dataframe
"""

from nltk.tokenize import word_tokenize

def tokenize_words(df):
  df['tokenized_title'] = df['Title_without_stopwords'].apply(word_tokenize)
  df['tokenized_text'] = df['Text_without_stopwords'].apply(word_tokenize)
  return df