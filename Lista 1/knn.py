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

# For each division (k-fold cross-validation)
total_execution_time_begin = time()
evaluations = []
for i in range(kfold + 1):
    kfold_execution_time_begin = time()

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

        kfold_execution_time_end = time()
        kfold_execution_time = kfold_execution_time_end - kfold_execution_time_begin
        percentage = float(rights)/len(evaluation) * 100
        evaluations.append(percentage)
        print 'K-Fold: ' + str(i)
        print 'Right predictions: ' + str(rights) + ' out of ' + str(len(evaluation)) + ' (' + str(round(percentage, 2)) + '%)'
        print  'Execution time: ' + str(kfold_execution_time) + ' seconds'
        print ""



mean = numpy.mean(evaluations)
std = numpy.std(evaluations)
total_execution_time_end = time()
total_execution_time = total_execution_time_end - total_execution_time_begin
print "Sucess rate mean: " + str(round(mean, 2)) + "%"
print "Sucess rate standard deviation: " + str(std)
print "Total execution time: " + str(total_execution_time) + ' seconds'