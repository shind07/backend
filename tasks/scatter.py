# -*- coding: utf-8 -*-
from common import scatter_data as data, agateToArray

columns = data.columns.keys();
defaults = columns[0:2]

def func(**kwargs):
    columns = defaults if 'cols' not in kwargs else kwargs['cols']
    subset = data.select(columns)
    print("kwargs:", kwargs)
    return agateToArray(subset)

def select(**kwargs):
    return list(columns)
