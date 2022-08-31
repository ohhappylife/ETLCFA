import nltk
from nltk.corpus import stopwords

def remove_stopwords(df):
  stop = set(stopwords.words('english'))
  df['Title_without_stopwords'] = df.apply(lambda row: nltk.word_tokenize(row['Title']), axis=1)
  df['Text_without_stopwords'] = df.apply(lambda row: nltk.word_tokenize(row['Text']), axis=1)

  df['Title_without_stopwords'] = df['Title_without_stopwords'].apply(
    lambda words: [word for word in words if word not in stop])
  df['Text_without_stopwords'] = df['Text_without_stopwords'].apply(
    lambda words: [word for word in words if word not in stop])

  df['Title_without_stopwords'] = [' '.join(map(str, l)) for l in df['Title_without_stopwords']]
  df['Text_without_stopwords'] = [' '.join(map(str, l)) for l in df['Text_without_stopwords']]
  return df
