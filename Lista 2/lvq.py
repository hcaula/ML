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
gen_prototypes = getattr(prototypes, args.prototype)

print gen_prototypes(p, dataset, classes)[0]
print gen_prototypes(p, dataset, classes)[1]