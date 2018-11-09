from common import scatter_data, agateToArray

def func(**kwargs):
    print("kwargs:", kwargs)
    return agateToArray(scatter_data)
