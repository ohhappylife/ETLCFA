from transform_general import remove_stop_words


def transofmr_politifact(df):
  df.loc[(df['Label'] == 'false'), 'Label'] = 'Fake'
  df.loc[(df['Label'] == 'pants-fire'), 'Label'] = 'Fake'
  df.loc[(df['Label'] == 'mostly-false'), 'Label'] = 'Fake'

  df.loc[(df['Label'] == 'half-true'), 'Label'] = 'Real'
  df.loc[(df['Label'] == 'true'), 'Label'] = 'Real'
  df.loc[(df['Label'] == 'mostly-true'), 'Label'] = 'Real'

  df.loc[(df['Label'] == 'Unverified'), 'Label'] = 'Unverified'

  df = df[df['Label'] != 'Unverified']
  df = df[df['Label'] != 'half-flip']
  df = df[df['Label'] != 'full-flip']
  df = df[df['Label'] != 'no-flip']

  remove_stop_words.remove_stopwords(df)

  df.dropna(subset=['Title'], inplace=True)
  df.drop(columns=['Label'])
  return df