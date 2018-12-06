# -*- coding: utf-8 -*-
from common import relationships_data, pandasToArray
import numpy as np

NUM_SELECTS = 1
data = relationships_data.sample(n=500)
columns = data.select_dtypes(np.number).columns.tolist()
data_columns_start = 0
defaults = columns[data_columns_start : data_columns_start + NUM_SELECTS]


def func(**kwargs):
    columns = defaults if 'col' not in kwargs else kwargs['col']
    subset = data[columns]
    return pandasToArray(subset)

def select(**kwargs):
    return columns[data_columns_start:]
