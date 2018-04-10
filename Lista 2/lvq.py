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

# def movement(p, x, add):
#     new_point = p
#     for attr in p:
#         if(add): new_point[attr] += alpha * (x[attr] - p[attr])
#         else: new_point[attr] -= alpha * (x[attr] - p[attr])
#     return new_point

# def lvq_1():
#     for r in range(repetitions)
#         count = 0
#         for x in dataset:
#             for p in prots:
#                 closest = 
        
