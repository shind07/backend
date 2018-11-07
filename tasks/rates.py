from common import rates

def func():
    return [rates[0]] + [ [rates[j][0]] + [float(i) for i in rates[j][1:]] for j in range(1, len(rates))]
