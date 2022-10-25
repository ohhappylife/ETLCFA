from keybert import KeyBERT

def summarize(df):
  # No model is supplied; default model = cnn
  keybert = KeyBERT()
  keywords = keybert.extract_keywords(
    df["Text"],
    keyphrase_ngram_range=(1, 1),
    stop_words='english',
    use_mmr=True,
    diversity=0.7
  )
  df["keywords"] = [k[0] for k in keywords]
  return df