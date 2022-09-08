"""
  save_csv_file.py
  save dataframe into cwd at current working directory
    param : dataframe, output folder name, output file name
    requirements : Users shall have privileges to save the file into a cwd.
    input : dataframe
    output : csv file
"""
__author__ = "Shon"
__version__ = "1.0.1"
__email__ = "sshon2@alumni.jh.edu"
__status__ = "Production"

import os

def save_file(df, folder_name, file_name):
  """
  Receive dataframe and store it as csv file into cwd.
  :param dataframe df : dataframe to be saved
         str folder_name : folder name to be stored
         str file_name: file name to be saved
  :return: None
  :rtype: None
  """
  cwd = os.getcwd()
  filename = file_name + ".csv"
  fileloc = os.path.join(cwd, folder_name)
  if not os.path.exists(fileloc):
    os.mkdir(fileloc)

  df.to_csv(f"{fileloc}/{filename}", header=True, index=False, encoding='utf-8')