
import pandas as pd
import sys
import os

n = len(sys.argv)
if n == 4:
  input_file_name = sys.argv[0]
  output_file_name = sys.argv[1]
  tokenized = sys.argv[2]
  Ngram = sys.argv[3]
else:
  raise Exception("Please enter the required arguments {input_file_name} {output_file_name} {tokenized} {Ngram}")


