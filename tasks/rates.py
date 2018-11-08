from common import rates, agateToArray

def func(**kwargs):
    print("kwargs:", kwargs)
    data = rates
    if "Year" in kwargs:
        data = data.where(lambda row: row["Year"] in kwargs["Year"])
    return agateToArray(data)

def values():
    pass
