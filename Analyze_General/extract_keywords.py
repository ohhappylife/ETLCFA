from keybert import KeyBERT

def summarize(df, col):
  keybert = KeyBERT()
  keywords = keybert.extract_keywords(
    df[col],
    keyphrase_ngram_range=(1, 1),
    stop_words='english',
    use_mmr=True,
    diversity=0.7
  )
  i = 0
  for keyword in keywords:
    if len(keyword) ==0:
      keywords[i] = "not available"
    i = i + 1
  df[col+"_keywords"] = [k[0] for k in keywords]
  return df