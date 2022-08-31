from nltk.tokenize import word_tokenize

def tokenize_words(df):
  df['tokenized_title'] = df['Title_without_stopwords'].apply(word_tokenize)
  df['tokenized_text'] = df['Text_without_stopwords'].apply(word_tokenize)
  return df