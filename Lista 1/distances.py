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

probabilities = {}
def precalc_partials(dataset):
    partials = {}
    totals = []

    # Calculates each partial sum for each class
    for d in dataset:
        c = d[len(d)-1]
        if(c not in partials): 
            partials[c] = []
            probabilities[c] = []
        
        count = 0
        for i in d:
            if (count < len(d)-1):
                if(len(partials[c]) <= count): 
                    partials[c].append({})
                    probabilities[c].append({})

                if(i not in partials[c][count]): 
                    partials[c][count][i] = 1
                    probabilities[c][count][i] = 0
                else: partials[c][count][i] += 1
            count += 1

    # Calculates total sum for each attribute
    for c in partials:
        count = 0
        for pos in partials[c]:
            if(len(totals) <= count): totals.append({})
            
            for attr in pos:
                if(attr not in totals[count]): totals[count][attr] = 0
                totals[count][attr] += partials[c][count][attr]
            count += 1
    
    # Calculates probability for each class for each attribute
    for c in partials:
        count = 0
        for pos in partials[c]:
            for attr in partials[c][count]:
                p = float(partials[c][count][attr])
                t = float(totals[count][attr])
                probabilities[c][count][attr] = p/t
            
            count += 1