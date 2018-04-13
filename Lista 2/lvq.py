# Custom libs
import prototypes
import distances
from precalcs import get_classes
from knn import knn
from data_reader import read
from args import args
from nn import nn

# Getting the arguments
dataset = read(args.d)
k = args.k
p = args.p
classes = get_classes(dataset)
repetitions = args.r
window = args.window
division = args.split

gen_prototypes = getattr(prototypes, args.prototype)
prots = gen_prototypes(p, dataset, classes)

distance = getattr(distances, args.distance)

training_size_index = int(len(dataset) * division)
training = dataset[0 : training_size_index]
evaluation = dataset[training_size_index: len(dataset)]

alpha = 0.01

def window_rule(x, m, n):
    s = (1-window)/(1+window)
    dm = distance(x, m)
    dn = distance(x, n)
    min_dist = min(dm/dn, dn/dm)

    if(min_dist > s): return True
    else: return False

def movement(p, x, add):
    for attr in range(len(p)):
        if(type(p[attr]) is int or type(p[attr]) is float):
            change = alpha * (x[attr] - p[attr])
            if(add): p[attr] += change
            else: p[attr] -= change


def lvq_1():
    for r in range(repetitions):
        for x in dataset:

            closest_prototype = nn(x, 1, prots)[0]
            closest_class = closest_prototype['class']
            x_class = x[len(x)-1]

            if(closest_class == x_class): movement(closest_prototype['elem'], x, True)
            else: movement(closest_prototype['elem'], x, False)
        
def lvq_2_1():
    prots_2_1 = prots[:]
    for r in range(repetitions):
        for x in dataset:
            closest_prototypes = nn(x, 2, prots)
            m = closest_prototypes[0]['elem']
            n = closest_prototypes[1]['elem']

            m_class = closest_prototypes[0]['class']
            n_class = closest_prototypes[1]['class']
            x_class = x[len(x)-1]

            same_class = m
            if(m_class == x_class):
                same_class = m
                other_class = n
            elif(n_class == x_class): 
                same_class = n
                other_class = m
            else: same_class = False

            if(window_rule(x,m,n) and same_class and m_class != n_class): 
                movement(same_class, x, True)
                movement(other_class, x, False)


lvq_1()
print prots
lvq_2_1()
print prots
