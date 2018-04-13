# External libs
from time import time
import numpy

# Custom libs
import distances
from args import args
from data_reader import read
from precalcs import precalcs
from precalcs import swap_array

def knn(k, training, evaluation):
    # Getting the arguments
    distance = getattr(distances, args.distance)
    w = args.w

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
        if(real_class == prediction): rights += 1

    percentage = float(rights)/len(evaluation) * 100
    print 'Right predictions: ' + str(rights) + ' out of ' + str(len(evaluation)) + ' (' + str(round(percentage, 2)) + '%)'