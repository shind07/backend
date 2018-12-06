# -*- coding: utf-8 -*-
from common import relationships_data, pandasToArray

NUM_SELECTS = 2
data = relationships_data.sample(n=2000)
columns = list(data.columns);
data_columns_start = 0
defaults = columns[data_columns_start:data_columns_start+NUM_SELECTS]


def func(**kwargs):
    cols= defaults if 'cols' not in kwargs else kwargs['cols']
    subset = data[cols]
    return pandasToArray(subset)

def select(**kwargs):
    return columns[data_columns_start:]
