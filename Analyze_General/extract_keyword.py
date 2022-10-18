from transformers import pipeline

def get_keyword(df):
  summarizer = pipeline("summarization")
  df['summarized_text'] = [x['summary_text'] for x in summarizer(df['Text'].tolist(), max_length=150)]
# df['summary'] = df.apply(lambda x: smr_bart(x['Text'], max_length=150)[0]['summary_text'] , axis=1)
  return df