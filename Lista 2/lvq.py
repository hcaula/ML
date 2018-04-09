# Custom libs
from knn import knn
from data_reader import read
from args import args

# Getting the arguments
dataset = read(args.d)
k = args.k