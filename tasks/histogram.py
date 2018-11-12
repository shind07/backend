from common import histogram_data, agateToArray

def func(**kwargs):
    print("kwargs:", kwargs)
    return agateToArray(histogram_data)
