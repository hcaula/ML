# Custom libs
from knn import knn
from data_reader import read
from args import args
from nn import nn

# Getting the arguments
dataset = read(args.d)
k = args.k

print nn(dataset[0], k, dataset)