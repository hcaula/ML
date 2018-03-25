# Importing libs
import argparse
import arff
import distances

# Setting command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-d', required=True, help='The dataset file in .arff')
parser.add_argument('-k', default=2, type=int, help='The k value for the k-NN')
parser.add_argument('-w', action='store_true', help='If the distance should be weighted or not')
parser.add_argument('-distance', default='euclidean', choices=['euclidean', 'vdm', 'hvdm'], help='The type of distance used for calculations')
parser.add_argument('-kfold', type=int, default=5, help='The k value for the k-fold cross-validation')

# Getting the arguments
args = parser.parse_args()
dataset = arff.load(open(args.d, 'rb'))['data']
kfold = args.kfold
distance = getattr(distances, args.distance)

# k-NN algorithm
dsize = len(dataset)
ksize = dsize/kfold

for i in range(kfold + 1):
    begin_index = i * ksize
    end_index = min((begin_index + ksize), dsize-1)

    evaluation = dataset[begin_index: end_index]
    training = dataset[0:begin_index] + dataset[end_index:dsize-1]