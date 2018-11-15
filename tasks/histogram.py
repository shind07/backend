# -*- coding: utf-8 -*-
from common import nba_data as data, agateToArray

NUM_SELECTS = 1
columns = list(data.columns.keys());
data_columns_start = 1
defaults = columns[data_columns_start:data_columns_start+NUM_SELECTS]

def func(**kwargs):
    columns = defaults if 'cols' not in kwargs else kwargs['cols']
    subset = data.select(columns)
    return agateToArray(subset)

def select(**kwargs):
    return columns[data_columns_start:]
