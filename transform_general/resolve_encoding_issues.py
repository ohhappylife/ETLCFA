import pandas as pd

def resolveEncodeIssue(df):
  """
  Temp method; this will resolve some common encoding issues
  :param dataframe df: dataframe to be cleaned
  :return: cleaned dataframe
  :rtype: dataframe
  """
  col = list(df.columns)
  for c in col:
    df[c] = df[c].astype(str).str.replace("“", "\"")
    df[c] = df[c].astype(str).str.replace("”", "\"")
    df[c] = df[c].astype(str).str.replace("‘", "\'")
    df[c] = df[c].astype(str).str.replace("’", "\'")
    df[c] = df[c].astype(str).str.replace("`", "\'")
    df[c] = df[c].astype(str).str.replace("–", ":")
    df[c] = df[c].astype(str).str.replace("…", "...")
    df[c] = df[c].astype(str).str.replace("…", "...")

    df['Site_url'] = df['Site_url'].astype(str).str.replace(".com//", ".com/")

    df.to_csv('one.csv', encoding='utf-8')
    df = pd.read_csv('one.csv')
    return df

import html

def HTMLtoChar(df, col_name):
  """
  Temp method; this will convert HTML characters to characters
  :param dataframe df: dataframe to be cleaned, String col_name : column that contains HTML char.
  :return: cleaned dataframe
  :rtype: dataframe
  """
  df[col_name] = df[col_name].apply(lambda x: html.unescape(x))
  return df