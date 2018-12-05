# -*- coding: utf-8 -*-
from common import pps_action_data, pandasToArray
import numpy as np

def func(**kwargs):
    return pandasToArray(pps_action_data)
