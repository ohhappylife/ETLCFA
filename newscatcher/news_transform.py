from transform_general import remove_stop_words


def remove_stopwords(df):
  df = remove_stop_words.remove_stopwords(df)
  return df