# Custom libs
import prototypes
import precalcs
from knn import knn
from data_reader import read
from args import args
from nn import nn

# Getting the arguments
dataset = read(args.d)
k = args.k
p = args.p
gen_prototypes = getattr(prototypes, args.prototype)