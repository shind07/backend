# -*- coding: utf-8 -*-
from common import nba_data, pandasToArray
import numpy as np

NUM_SELECTS = 1
columns = ['Year'] + nba_data.select_dtypes(np.number).columns.tolist()
data_columns_start = 1
defaults = columns[data_columns_start : data_columns_start + NUM_SELECTS]

def func(**kwargs):
    data = nba_data
    stat = defaults if 'col' not in kwargs else kwargs['col']
    multi_index = False;
    if 'teams' in kwargs:
        data = data[data['Team'].isin(kwargs['teams'])]
    if 'grouped' not in kwargs or kwargs['grouped'][0] == 'true':
        data = data.groupby('Year', as_index=False)[stat].mean()
    else:
        data = data.pivot(index='Year', columns='Team', values=stat)
        data.reset_index(inplace=True)
    return pandasToArray(data)

def select_columns(**kwargs):
    return columns[data_columns_start:]

def select_years(**kwargs):
    return sorted(list(nba_data["Team"].unique()))
