# -*- coding: utf-8 -*-
from common import nba_data as data, pandasToArray
import numpy as np

NUM_SELECTS = 1
columns = ['Year'] + data.select_dtypes(np.number).columns.tolist()

data_columns_start = 1
defaults = columns[data_columns_start : data_columns_start + NUM_SELECTS]

def func(**kwargs):
    grouping_column = defaults if 'cols' not in kwargs else kwargs['cols']
    grouped = data.groupby('Year', as_index=False)[grouping_column].mean()
    return pandasToArray(grouped)

def select_columns(**kwargs):
    return columns[data_columns_start:]

def select_teams(**kwargs):
    pass
