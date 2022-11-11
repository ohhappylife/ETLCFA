"""
  load_csv_file.py
  load csv file from the current working directory
    requirements : csv formatted files shall be in the cwd
    input : csv file
    output : dataframe
"""
__author__ = "Shon"
__version__ = "1.0.1"
__email__ = "sshon2@alumni.jh.edu"
__status__ = "Production"

import os
import pandas as pd
from csv import reader
import csv
def load_file(file_name):
  """
  Load csv file and store it as dataframe
  :param str file_name: file name to be imported
  :return: imported file
  :rtype: dataframe
  """
  cwd = os.getcwd()
  fileloc = ""
  fileloc = os.path.join(cwd, fileloc)

  if os.path.isfile(file_name):
    try:
      extension = file_name[-4:len(str(file_name))]
      if (extension == ".csv") | (extension == ".txt"):
        file_name = fileloc + file_name
      else:
        file_name = fileloc + file_name + ".csv"
    except IndexError:
      file_name = fileloc + file_name + "csv"
  else:
    raise Exception("file does not exist")
  df = pd.read_csv(file_name)
  return df

def readLinebyLine(file_name):
  ls = []
  fn = str(file_name)
  with open(fn, 'r') as read_obj:
    reader = csv.reader(read_obj)
    data = list(reader)
    for d in data:
      ls.append(str(d).split("=")[1].replace("'","").replace("]",""))
      print(d)
      print(ls)
    return ls