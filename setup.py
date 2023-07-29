'''
Util script for downloading the startup investmens data.
'''
import opendatasets

DATA_DIR = 'data'
DATA_URL = 'https://www.kaggle.com/datasets/justinas/startup-investments'

opendatasets.download(
    DATA_URL,
    data_dir=DATA_DIR,
  )
