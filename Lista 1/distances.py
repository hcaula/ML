import math

def euclidean(x, y):
    size = len(x)
    sum = 0
    for i in range(size): 
        if((type(x[i]) is int or type(x[i]) is float) and (type(y[i]) is int or type(y[i]) is float)): 
            sum += pow((x[i] - y[i]), 2)
    return math.sqrt(sum)

def vdm(x, y):
    return 2

partials = {}
totals = []
def precalc_partials(dataset):

    # Gets the classes
    for d in dataset:
        c = d[len(d)-1]
        if(c not in partials): 
            partials[c] = []
        
        count = 0
        for i in d:
            if (count < len(d)-1):
                if(len(partials[c]) <= count): partials[c].append({})

                if(i not in partials[c][count]): partials[c][count][i] = 1
                else: partials[c][count][i] += 1
            count += 1

    for c in partials:
        count = 0
        for pos in partials[c]:
            if(len(totals) <= count): totals.append({})
            
            for attr in pos:
                if(attr not in totals[count]): totals[count][attr] = 0
                totals[count][attr] += partials[c][count][attr]
            count += 1