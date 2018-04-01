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
    print "Dataset length: " + str(len(dataset))
    print ""
    # Gets the classes
    probs = {}
    for d in dataset:
        c = d[len(d)-1]
        if(c not in probs): probs[c] = []
        
        count = 0
        for i in d:
            if (count < len(d)-1):
                if(len(probs[c]) <= count): probs[c].append({})
                if(i not in probs[c][count]): probs[c][count][i] = 1
                else: probs[c][count][i] += 1
            count += 1

    print probs

    