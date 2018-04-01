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

probabilities = {}
def precalc_probs(dataset):

    # Gets the classes
    totals = {}
    for d in dataset:
        c = d[len(d)-1]
        if(c not in totals): 
            totals[c] = []
            probabilities[c] = []
        
        count = 0
        for i in d:
            if (count < len(d)-1):
                if(len(totals[c]) <= count): 
                    totals[c].append({})
                    probabilities[c].append({})

                if(i not in totals[c][count]): 
                    totals[c][count][i] = 1
                    probabilities[c][count][i] = 0
                else: totals[c][count][i] += 1
            count += 1

    print totals