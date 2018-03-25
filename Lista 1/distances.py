import math

def euclidean(x, y):
    sum = 0
    for attr in x: sum += pow(x[attr] - y[attr], 2)
    return math.sqrt(sum)
    

def vdm(x, y):
    return 2