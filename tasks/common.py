import csv, os, agate
import pandas as pd
from decimal import Decimal
from config import data_dir

def csvToArray(path):
    with open(path) as f:
        csv_reader = csv.reader(f)
        return [row for row in csv_reader]

def agateToArray(table):
    return [list(table.column_names)] + [
        [round(float(i), 2) if isinstance(i, Decimal) else i if i is not None else "" for i in row]
        for row in table]

def pandasToArray(table):
    columns = list(table.columns) if type(table.columns) != pd.MultiIndex else \
        [table.columns[0][0]] + [col[1] for col in table.columns[1:]]
    return [columns] + table.round(2).values.tolist()



tester = agate.TypeTester(force={
    'Year': agate.Text()
})

sample_data = csvToArray(os.path.join(data_dir, 'sample.csv'))


nba_data = pd.read_csv(os.path.join(data_dir, 'nba_trends.csv'))
nba_data['Team'] = nba_data['Team'].apply(lambda team: team[:-1] if '*' in team else team)

pps_shot_clock_data = pd.read_csv(os.path.join(data_dir, 'pps_shot_clock.csv'))
pps_action_data = pd.read_csv(os.path.join(data_dir, 'pps_action.csv'))

relationships_data = pd.read_csv(os.path.join(data_dir, 'box_relationships.csv'))
# get all float columns
