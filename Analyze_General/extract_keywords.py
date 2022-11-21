from keybert import KeyBERT

def summarize(df, col):
  # No model is supplied; default model = cnn
  keybert = KeyBERT()
  keywords = keybert.extract_keywords(
    df[col],
    keyphrase_ngram_range=(1, 1),
    stop_words='english',
    use_mmr=True,
    diversity=0.7
  )
  df["keywords_" + col] = [k[0] for k in keywords]
  return df