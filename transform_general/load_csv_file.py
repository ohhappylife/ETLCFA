import os
import pandas as pd

def load_file(file_name):
  cwd = os.getcwd()
  fileloc = "files"
  fileloc = os.path.join(cwd, fileloc)

  if os.path.isfile(file_name):
    try:
      extension = file_name[-4]
      if extension == ".csv":
        file_name = fileloc + file_name
      else:
        file_name = fileloc + file_name + ".csv"
    except IndexError:
      file_name = fileloc + file_name + "csv"
  else:
    raise Exception("file does not exist")
  df = pd.read_csv(file_name)
  return df