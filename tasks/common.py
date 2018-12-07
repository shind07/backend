import csv, os
import pandas as pd
from decimal import Decimal
from config import data_dir

def csvToArray(path):
    with open(path) as f:
        csv_reader = csv.reader(f)
        return [row for row in csv_reader]

def pandasToArray(table):
    columns = list(table.columns) if type(table.columns) != pd.MultiIndex else \
        [table.columns[0][0]] + [col[1] for col in table.columns[1:]]
    return [columns] + table.round(2).values.tolist()

assists_action_data = pd.read_csv(os.path.join(data_dir, 'assists_action.csv'))
assists_player_data = pd.read_csv(os.path.join(data_dir, 'assists_player.csv'))
pps_shot_clock_data = pd.read_csv(os.path.join(data_dir, 'pps_shot_clock.csv'))
pps_action_data = pd.read_csv(os.path.join(data_dir, 'pps_action.csv'))
relationships_data = pd.read_csv(os.path.join(data_dir, 'box_relationships.csv'))
trends_data = pd.read_csv(os.path.join(data_dir, 'box_trends.csv'))
# get all float columns
