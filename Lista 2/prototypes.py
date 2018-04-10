# Module for generating prototypes
from random import randint

# Generates random attributes limited to the max and min of the dataset
def limited(n, dataset, classes):
    prototypes = []
    sample = dataset[0]

    # For each attribute for a sample in the dataset
    for attr in range(len(sample)):
        max_attr = max(dataset, key=lambda x: x[attr])[attr]
        min_attr = min(dataset, key=lambda x: x[attr])[attr]

        # For each possible class
        for c in range(len(classes)): 
            if(c >= len(prototypes)): prototypes.append([])

            # For each number of prototype
            for p in range(n):
                if(p >= len(prototypes[c])): prototypes[c].append([])

                elem = 0
                if(type(sample[attr]) is int or type(sample[attr]) is float): elem = randint(int(min_attr), int(max_attr))
                elif(attr < len(sample)-1): elem = sample[attr]
                else: elem = classes[c]

                if(attr >= len(prototypes[c][p])): prototypes[c][p].append(0)
                prototypes[c][p][attr] = elem

    linear_list = []
    for i in range(len(prototypes)):
        for j in range(len(prototypes[i])): linear_list.append(prototypes[i][j])
    return linear_list