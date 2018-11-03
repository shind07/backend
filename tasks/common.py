import csv, os
from config import data_dir

def csvToList(path):
    with open(path) as f:
        csv_reader = csv.reader(f)
        return [row for row in csv_reader]

path = os.path.join(data_dir, 'sample.csv')
sample_data = csvToList(os.path.join(data_dir, 'sample.csv'))
