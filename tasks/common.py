import csv, os, agate
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

tester = agate.TypeTester(force={
    'Year': agate.Text()
})

rates = agate.Table.from_csv(os.path.join(data_dir, 'rates.csv'), column_types=tester)
sample_data = csvToArray(os.path.join(data_dir, 'sample.csv'))

scatter_data = agate.Table.from_csv(os.path.join(data_dir, 'scatter.csv'))
