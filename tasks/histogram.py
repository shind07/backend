# -*- coding: utf-8 -*-
from common import nba_data as data, agateToArray, pandasToArray
import numpy as np

NUM_SELECTS = 1
columns = list(data.columns)
data_columns_start = 2
defaults = columns[data_columns_start : data_columns_start + NUM_SELECTS]

def func(**kwargs):
    columns = defaults if 'cols' not in kwargs else kwargs['cols']
    #subset = data.select(columns)
    subset = data[columns]
    return pandasToArray(subset.select_dtypes(np.number))

def select(**kwargs):
    return columns[data_columns_start:]
