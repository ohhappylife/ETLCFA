"""
  politifact_transform.py
  Clear the crawled data (Politifact)
    requirements : Crawled data shall be exists.
    input : dataframe
    output : dataframe
  [False, pants-frie, mostly-false, barely-true] : Fake
  [half-true, true, mostly true] : real
  [Unverified, half-flip, full-flip, no-flip] : dropped from the df
  tuples without title will be dropped.
"""
__author__ = "Shon"
__version__ = "1.0.1"
__email__ = "sshon2@alumni.jh.edu"
__status__ = "Production"

def transofmr_politifact(df):
  """
  Transform the collected dataset.
  :param dataframe df: collected news articles and transform articles.
  :return: cleaned news articles
  :rtype: dataframe
  """
  df.loc[(df['Label'] == 'false'), 'Label'] = 'Fake'
  df.loc[(df['Label'] == 'pants-fire'), 'Label'] = 'Fake'
  df.loc[(df['Label'] == 'mostly-false'), 'Label'] = 'Fake'
  df.loc[(df['Label'] == 'barely-true'), 'Label'] = 'Fake'

  df.loc[(df['Label'] == 'half-true'), 'Label'] = 'Real'
  df.loc[(df['Label'] == 'true'), 'Label'] = 'Real'
  df.loc[(df['Label'] == 'mostly-true'), 'Label'] = 'Real'

  df.loc[(df['Label'] == 'Unverified'), 'Label'] = 'Unverified'

  df = df[df['Label'] != 'Unverified']
  df = df[df['Label'] != 'half-flip']
  df = df[df['Label'] != 'full-flip']
  df = df[df['Label'] != 'full-flop']
  df = df[df['Label'] != 'no-flip']

  df.dropna(subset=['Title'], inplace=True)
  df.drop(columns=['Label'])
  return df