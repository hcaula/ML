# External libs
import argparse
import arff
from random import shuffle

# Custom libs
import distances

# Setting command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-d', required=True, help='The dataset file in .arff')
parser.add_argument('-k', default=2, type=int, help='The k value for the k-NN')
parser.add_argument('-w', action='store_true', help='If the distance should be weighted or not')
parser.add_argument('-distance', default='euclidean', choices=['euclidean', 'vdm', 'hvdm'], help='The type of distance used for calculations')
parser.add_argument('-kfold', type=int, default=5, help='The k value for the k-fold cross-validation')
parser.add_argument('-shuffle', action='store_true', help='If the dataset should be randomly shuffled before k-fold')
args = parser.parse_args()

# Getting the arguments
kfold = args.kfold
k = args.k
distance = getattr(distances, args.distance)
dataset = arff.load(open(args.d, 'rb'))['data']

## Shuffles dataset if it's said so
if (args.shuffle): shuffle(dataset)

# k-NN algorithm
dsize = len(dataset)
ksize = dsize/kfold

## For each division (k-fold cross-validation)
for i in range(kfold + 1):
    begin_index = i * ksize
    end_index = min((begin_index + ksize), dsize-1)

    evaluation = dataset[begin_index: end_index]
    training = dataset[0:begin_index] + dataset[end_index:dsize-1]

    test = []
    for e in evaluation:
        dists = []
        tests = []
        for t in training: 
            dist = distance(e, t)
            t_class = t[len(t)-1] in ['True', 'true']

            obj = {'distance': dist, 'class': t_class}
            dists.append(obj)

        # Sorts the distances and gets the k-nearest neighbours
        dists.sort(key=lambda x: x['distance'])
        neighbours = dists[0:k]
