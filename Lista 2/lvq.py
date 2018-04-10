# Custom libs
import prototypes
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
gen_prototypes = getattr(prototypes, args.prototype)
prots = gen_prototypes(p, dataset, classes)

alpha = 0.1

print prots

# def movement(p, x, add):
#     for attr in p:
#         if(add): p[attr] += alpha * (x[attr] - p[attr])
#         else: p[attr] -= alpha * (x[attr] - p[attr])

# def lvq_1():
#     for r in range(repetitions):
#         for x in dataset:
#             closest_prototype = nn(x, prots)
#             closest_class = closest_prototype['class']
#             x_class = x[len(x)-1]

#             if(closest_class == x_class): movement(p, x, True)
#             else: movement(p, x, False)

# # print prots
# lvq_1()
# print prots
        
