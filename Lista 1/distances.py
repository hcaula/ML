import math

def euclidean(x, y, dataset):
    size = len(x)
    sum = 0
    for i in range(size): 
        if((type(x[i]) is int or type(x[i]) is float) and (type(y[i]) is int or type(y[i]) is float)): 
            sum += pow((x[i] - y[i]), 2)
    return math.sqrt(sum)

def vdm(x, y, dataset):
    return 2
    # size = len(x)
    # sum = 0
    # for i in range(size): 
    #     if(not hasattr(probabilites, x[i])):
    #         calculate_probability

probabilites = {}
def precalc_probs(dataset):
    # Gets the classes
    classes = []
    for d in dataset:
        clss = d[len(d)-1]
        if(clss not in classes): classes.append(clss)
    
