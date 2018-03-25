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
evaluations = []
for i in range(kfold + 1):
    begin_index = i * ksize
    end_index = min((begin_index + ksize), dsize-1)

    ## If the k-fold divides the training set perfectly, we shouldn't run the last k-fold
    if end_index > begin_index:
        rights = 0

        evaluation = dataset[begin_index: end_index]
        training = dataset[0:begin_index] + dataset[end_index:dsize-1]

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

            ## Checking if the last fold has less elements the chosen k
            end_index = min(k, len(dists)-1)
            neighbours = dists[0:end_index]

            # Counts the number of classes for the k-nearests neighbours
            pos = 0
            neg = 0
            for n in neighbours:
                if(n['class']): pos += 1
                else: neg += 1
            
            # If there are more positives than negatives, set prediction as True
            prediction = False
            if(pos >= neg): prediction = True
            
            # Checks if prediction was correct
            

            real_class = e[len(e)-1] in ['True', 'true']
            if(real_class == prediction): rights += 1

        print 'K-Fold: ' + str(i)
        print 'Right predictions: ' + str(rights) + ' out of ' + str(len(evaluation))
