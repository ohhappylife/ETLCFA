import nltk
from keybert import KeyBERT
import yake
def summarize(df, col):
  df['keyword_'+col] = 'missing'
  language = 'en'
  max_ngram_size = 3
  deduplication_threshold = 0.9
  numOfKeywords = 3
  custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size,
                                              dedupLim=deduplication_threshold,
                                              top=numOfKeywords, features=None)

  extract_keywords = lambda x: [k[0] for k in custom_kw_extractor.extract_keywords(x)]
  df['keyword_'+col] = df[col].apply(extract_keywords)
  return df