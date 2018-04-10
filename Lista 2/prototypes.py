# Module for generating prototypes
import random

# Generates random attributes limited to the max and min of the dataset
def limited(n, dataset):
    prototypes = []
    for attr in range(len(dataset[0])):
        max_attr = max(dataset, key=lambda x: x[attr])[attr]
        min_attr = min(dataset, key=lambda x: x[attr])[attr]
        for i in range(n):
            if(len(prototypes) <= i): prototypes.append([])
            if(len(prototypes[i]) <= attr): prototypes[i].append(0)
            
            # If the attribute is a number, generate a random. Otherwise, get the sample's attribute.
            if(type(dataset[0][attr]) is int or type(dataset[0][attr]) is float):
                prototypes[i][attr] = random.randint(int(min_attr), int(max_attr))
            else: prototypes[i][attr] = dataset[0][attr]
    return prototypes