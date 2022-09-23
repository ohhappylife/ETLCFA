import pandas as pd
def resolveEncodeIssue(df):
  col = list(df.columns)
  for c in col:
    df[c] = df[c].astype(str).str.replace("“", "\"")
    df[c] = df[c].astype(str).str.replace("”", "\"")
    df[c] = df[c].astype(str).str.replace("‘", "\'")
    df[c] = df[c].astype(str).str.replace("’", "\'")
    df[c] = df[c].astype(str).str.replace("–", ":")
    df[c] = df[c].astype(str).str.replace("…", "...")

    df['Site_url'] = df['Site_url'].astype(str).str.replace(".com//", ".com/")

    df.to_csv('one.csv', encoding='utf-8')
    df = pd.read_csv('one.csv')
    return df
