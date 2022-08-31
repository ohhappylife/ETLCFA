import os

def save_file(df, name):
  cwd = os.getcwd()
  filename = name + ".csv"
  fileloc = os.path.join(cwd, filename)
  if not os.path.exists(fileloc):
    os.mkdir(fileloc)

  df.to_csv(f"{fileloc}/{filename}", header=True, index=False, encoding='utf-8')