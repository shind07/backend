# -*- coding: utf-8 -*-
from common import nba_data as data, pandasToArray
import numpy as np

NUM_SELECTS = 1
columns = list(data.columns)
data_columns_start = 2
defaults = columns[data_columns_start : data_columns_start + NUM_SELECTS]

def func(**kwargs):
    print("kwargs:", kwargs)
    return agateToArray(data)

def select(**kwargs):
    return columns[data_columns_start:]
