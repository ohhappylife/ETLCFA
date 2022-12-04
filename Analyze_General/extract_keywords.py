from config import summarizer_numOfKeywords, summarizer_deduplication_threshold, summarizer_max_ngram_size
import yake
def get_keywords(df, col):
  df['keyword_'+col] = 'missing'
  language = 'en'
  custom_kw_extractor = yake.KeywordExtractor(lan=language,
                                              n=summarizer_max_ngram_size,
                                              dedupLim=summarizer_deduplication_threshold,
                                              top=summarizer_numOfKeywords,
                                              features=None)

  extract_keywords = lambda x: [k[0] for k in custom_kw_extractor.extract_keywords(x)]
  df['keyword_'+col] = df[col].apply(extract_keywords)
  return df