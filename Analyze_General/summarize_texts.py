from transformers import pipeline
from config import summary_max_length, summary_min_length

def get_keyword(df):
  summarizer = pipeline("summarization")
  df['summarized_text'] = [x['summary_text'] for x in summarizer(df['Text'].tolist(), min_length=summary_min_length ,max_length=summary_max_length)]
  return df