# -*- coding: utf-8 -*-
from common import histogram_data as data, agateToArray

def func(**kwargs):
    print("kwargs:", kwargs)
    return agateToArray(data)

def select(**kwargs):
    return list(data.columns.keys())[1:]
