from transformers import pipeline

def get_keyword(df):
  summarizer = pipeline("summarization")
  df["summarized_text"] = summarizer(df["Text"].to_string(), truncation=True)[0]['summary_text']
  return df