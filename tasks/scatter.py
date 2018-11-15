# -*- coding: utf-8 -*-
from common import nba_data as data, pandasToArray

NUM_SELECTS = 2
columns = list(data.columns);
data_columns_start = 2
defaults = columns[data_columns_start:data_columns_start+NUM_SELECTS]

def func(**kwargs):
    cols= defaults if 'cols' not in kwargs else kwargs['cols']
    subset = data[cols]
    return pandasToArray(subset)

def select(**kwargs):
    return columns[data_columns_start:]
