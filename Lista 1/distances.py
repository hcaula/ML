import math

def euclidean(x, y):
    size = len(x)
    sum = 0
    for i in range(size): 
        if(type(x[i]) is int or type(x[i]) is float): sum += pow((x[i] - y[i]), 2)
    return math.sqrt(sum)
    

def vdm(x, y):
    return 2