from nltk.tokenize import word_tokenize
from logger import logger
def tokenize_words(df):
  """
  Tokenize news articles for analysis.
  :param dataframe df: dataframe to be cleaned.
  :return: dataframe with tokenized article
  :rtype: dataframe
  """
  df['tokenized_title'] = df['Title_without_stopwords'].apply(word_tokenize)
  df['tokenized_text'] = df['Text_without_stopwords'].apply(word_tokenize)
  return df