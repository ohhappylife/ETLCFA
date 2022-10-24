from transformers import pipeline

def get_keyword(df):
  summarizer = pipeline("summarization")
  df['summarized_text'] = [x['summary_text'] for x in summarizer(df['Text'].tolist(), max_length=150)]
  return df