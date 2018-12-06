# -*- coding: utf-8 -*-
from common import trends_data, pandasToArray
import numpy as np

data = trends_data
NUM_SELECTS = 1
columns = ['Label'] + data.select_dtypes(np.number).columns.tolist()
data_columns_start = 2
defaults = columns[data_columns_start : data_columns_start + NUM_SELECTS]

def func(**kwargs):
    stat = defaults if 'col' not in kwargs else kwargs['col']
    piv = data.pivot(index='Year', columns='Label', values=stat)
    piv.reset_index(inplace=True)
    piv['Year'] = piv['Year'].apply(lambda x: str(x) + ' ')
    return pandasToArray(piv)

def select_columns(**kwargs):
    return columns[data_columns_start:]

def select_teams(**kwargs):
    return sorted(list(nba_data["Team"].unique()))
