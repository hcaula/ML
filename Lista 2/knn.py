# External libs
from time import time
from random import shuffle
import numpy

# Custom libs
import distances
import args
from data_reader import read
from precalcs import precalcs
from precalcs import swap_array

# Getting the arguments
arguments = args.args
kfold = arguments.kfold
k = arguments.k
distance = getattr(distances, arguments.distance)
dataset = read(arguments.d)
w = arguments.w
swap = arguments.swap

# Shuffles dataset if it's said so
precalcs_time_begin = time()

if (arguments.shuffle): shuffle(dataset)
if (arguments.distance != "euclidean"): precalcs(dataset)

precalcs_time_endtime = time()
precalcs_time = precalcs_time_endtime - precalcs_time_begin
if(swap): swap_array(dataset)
print "Pre-processing time: " + str(precalcs_time) + ' seconds'
print ""

# k-NN algorithm
dsize = len(dataset)
ksize = dsize/kfold
division = 0.6

# For each division (k-fold cross-validation)
total_execution_time_begin = time()
evaluations = []

training_size_index = int(len(dataset) * division)
training = dataset[0 : training_size_index]
evaluation = dataset[training_size_index: len(dataset)]

rights = 0
for e in evaluation:
    dists = []
    for t in training: 

        # Calculating the distance between the evaluated element to the training set
        dist = distance(e, t)
        if(w):
            p = pow(dist, 2)
            if(p>0): weight = 1/p
            else: weight = 1/0.001
        else: weight = 1

        new_dist = weight * dist

        obj = {'distance': new_dist, 'class': str(t[len(t)-1])}
        dists.append(obj)

    # Sorts the distances to get the k-nearest neighbours
    dists.sort(key=lambda x: x['distance'])

    # Cutting the array for the neighbours
    neighbours = dists[0:k]

    # Counts the number of classes for the k-nearests neighbours
    classes = {}
    for n in neighbours:
        if(n['class'] in classes): classes[n['class']] += 1
        else: classes[n['class']] = 1
    
    # Sets the prediction to be the class with most neighbours
    prediction = max(classes, key=classes.get)
        
    # Checks if prediction was correct
    real_class = e[len(e)-1]
    if(real_class == prediction): 
        rights += 1
        print real_class
        print neighbours

percentage = float(rights)/len(evaluation) * 100
evaluations.append(percentage)
print 'Right predictions: ' + str(rights) + ' out of ' + str(len(evaluation)) + ' (' + str(round(percentage, 2)) + '%)'