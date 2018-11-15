# -*- coding: utf-8 -*-
from common import nba_data as data, agateToArray

columns = data.columns.keys()[1:];
defaults = columns[0:2]

def func(**kwargs):
    columns = defaults if 'cols' not in kwargs else kwargs['cols']
    subset = data.select(columns)
    print("kwargs:", kwargs)
    return agateToArray(subset)

def select(**kwargs):
    return list(columns)
