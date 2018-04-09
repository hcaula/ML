import math
from precalcs import probabilities
from precalcs import ranges

def euclidean(x, y):
    size = len(x) - 1
    sum = 0
    for i in range(size): 
        test = (type(x[i]) is int or type(x[i]) is float) and (type(y[i]) is int or type(y[i]) is float)
        if(test): sum += pow((x[i] - y[i]), 2)
    return math.sqrt(sum)

def vdm(x, y):
    size = len(x) - 1
    total_sum = 0

    # For each attribute
    for i in range(size): total_sum += little_vdm(x[i], y[i], i)

    # Returns the square root of the total sum   
    return math.sqrt(total_sum)

def hvdm(x, y):
    size = len(x) - 1
    total_sum = 0

    count = 0
    for i in range(size):
        test = (type(x[i]) is int or type(x[i]) is float) and (type(y[i]) is int or type(y[i]) is float)
        if(test): total_sum += abs(x[i] - y[i]) / (ranges[count]["max"] - ranges[count]["min"])
        else: total_sum += little_vdm(x[i], y[i], i)
    return total_sum

def little_vdm(xa, ya, attr):
    # The normalization constant
    q = 1

    partial_sum = 0
    for c in probabilities:
        prob = probabilities[c][attr]
        
        prob_x = 0
        prob_y = 0
        if(xa in prob): prob_x = prob[xa]
        if(ya in prob): prob_y = prob[ya]

        sub = abs(prob_x - prob_y)
        normalized = (1 - sub/q)
        
        partial_sum += normalized
    return partial_sum