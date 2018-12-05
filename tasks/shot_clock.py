# -*- coding: utf-8 -*-
from common import pps_shot_clock_data, pandasToArray
import numpy as np

def func(**kwargs):
    return pandasToArray(pps_shot_clock_data)
