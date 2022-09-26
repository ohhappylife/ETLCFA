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
      extension = file_name[1:5]
      if (extension == ".csv") | (extension == ".txt"):
        file_name = fileloc + file_name
      else:
        file_name = fileloc + file_name + ".csv"
    except IndexError:
      file_name = fileloc + file_name + "csv"
  else:
    raise Exception("file does not exist")
  df = pd.read_csv(file_name)
  return file_name