probabilities = {}
ranges = []

def get_classes(dataset):
    classes = []
    for d in dataset:
        if(d[len(d)-1] not in classes): classes.append(d[len(d)-1])
    return classes

def precalcs(dataset):
    partials = {}
    totals = []

    sample = dataset[0]
    size = len(sample) - 1
    for i in range(size):
        if(type(sample[i]) is int or type(sample[i]) is float): 
            ranges.append({
                "max": max(map(lambda x: x[i], dataset)),
                "min": min(map(lambda x: x[i], dataset))
            })
        else: ranges.append({})


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

def swap_array(dataset):
    for d in dataset:
        length = len(d)-1
        temp = d[length]
        d[length] = d[0]
        d[0] = temp
