# Module to return the nearest class from element
import distances
from args import args

def nn(x, dataset):
    distance = getattr(distances, args.distance)
    dataset_copy = dataset[:]
    dataset_copy.remove(x)

    neighbour = {}
    for d in dataset_copy:
        dist = distance(x, d)
        elem = {'distance': dist, 'class': d[len(d)-1]}
        if(neighbour == {} or dist < neighbour['distance']): neighbour = elem
    
    return neighbour
