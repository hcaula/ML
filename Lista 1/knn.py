# External libs
import argparse
from random import shuffle

# Custom libs
import distances
import args
from data_reader import read

# Getting the arguments
arguments = args.args
kfold = arguments.kfold
k = arguments.k
distance = getattr(distances, arguments.distance)
dataset = read(arguments.d)

# Shuffles dataset if it's said so
if (arguments.shuffle): shuffle(dataset)

# k-NN algorithm
dsize = len(dataset)
ksize = dsize/kfold

# For each division (k-fold cross-validation)
for i in range(kfold + 1):
    begin_index = i * ksize
    end_index = min((begin_index + ksize), dsize-1)

    # If the k-fold divides the training set perfectly, we shouldn't run the last k-fold
    if end_index > begin_index:
        rights = 0

        evaluation = dataset[begin_index: end_index]
        training = dataset[0:begin_index] + dataset[end_index:dsize-1]

        for e in evaluation:
            dists = []
            for t in training: 

                # Calculating the distance between the evaluated element to the training set
                dist = distance(e, t)
                obj = {'distance': dist, 'class': str(t[len(t)-1])}
                dists.append(obj)

            # Sorts the distances to get the k-nearest neighbours
            dists.sort(key=lambda x: x['distance'])

            # Checking if the last fold has less elements the chosen k
            end_index = min(k, len(dists)-1)
            neighbours = dists[0:end_index]

            # Counts the number of classes for the k-nearests neighbours
            classes = {}
            for n in neighbours:
                if(n['class'] in classes): classes[n['class']] += 1
                else: classes[n['class']] = 1
            
            # Sets the prediction to be the class with most neighbours
            prediction = max(classes, key=classes.get)
            
            # Checks if prediction was correct
            real_class = e[len(e)-1]
            if(real_class == prediction): rights += 1

        print 'K-Fold: ' + str(i)
        print 'Right predictions: ' + str(rights) + ' out of ' + str(len(evaluation))
