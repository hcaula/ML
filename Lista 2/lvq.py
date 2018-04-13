# Custom libs
import prototypes
import distances
from precalcs import get_classes
from knn import knn
from data_reader import read
from args import args
from nn import nn
from random import shuffle

# Getting the arguments
dataset = read(args.d)
k = args.k
p = args.p
classes = get_classes(dataset)
repetitions = args.r
window = args.window
division = args.split
gen_repetitions = args.repetitions

training_size_index = int(len(dataset) * division)
training = dataset[0 : training_size_index]
evaluation = dataset[training_size_index: len(dataset)]

distance = getattr(distances, args.distance)

if (args.shuffle): shuffle(dataset)

alpha = 0.01
e = 2

def window_rule(x, m, n):
    s = (1-window)/(1+window)
    dm = distance(x, m)
    dn = distance(x, n)
    min_dist = min(dm/dn, dn/dm)

    if(min_dist > s): return True
    else: return False

def movement(p, x, add, e=1):
    for attr in range(len(p)):
        if(type(p[attr]) is int or type(p[attr]) is float):
            change = e * alpha * (x[attr] - p[attr])
            if(add): p[attr] += change
            else: p[attr] -= change


def lvq_1(prots):
    for r in range(repetitions):
        for x in dataset:

            closest_prototype = nn(x, 1, prots)[0]
            closest_class = closest_prototype['class']
            x_class = x[len(x)-1]

            if(closest_class == x_class): movement(closest_prototype['elem'], x, True)
            else: movement(closest_prototype['elem'], x, False)

    print "LVQ 1 RESULTS:"
    return {'results': knn(k, prots, evaluation), 'prots': prots}
        
def lvq_2_1(prots):
    prots_2_1 = prots[:]
    for r in range(repetitions):
        for x in dataset:
            closest_prototypes = nn(x, 2, prots_2_1)
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

    print "LVQ 2.1 RESULTS:"
    return knn(k, prots_2_1, evaluation)

def lvq_3(prots):
    prots_3 = prots[:]
    for r in range(repetitions):
        for x in dataset:
            closest_prototypes = nn(x, 2, prots_3)
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

            if(window_rule(x,m,n) and same_class):
                if(m_class != n_class):
                    movement(same_class, x, True)
                    movement(other_class, x, False)
                else:
                    movement(same_class, x, True, e=e)
                    movement(other_class, x, True, e=e)

    print "LVQ 3 RESULTS:"
    return knn(k, prots_3, evaluation)


def main():
    percentages = [[], [], []]
    for i in range(gen_repetitions):
        gen_prototypes = getattr(prototypes, args.prototype)
        prots = gen_prototypes(p, training, classes)

        print "Repetition " + str(i)
        lvq_1_res = lvq_1(prots)

        percentages[0].append(lvq_1_res['results'])
        modified_prots = lvq_1_res['prots']

        percentages[1].append(lvq_2_1(modified_prots))
        percentages[2].append(lvq_3(modified_prots))
        print ""

    print "All rates: "
    print percentages
main()