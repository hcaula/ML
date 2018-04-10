# Module to return the nearest class from element
import distances
from args import args

def nn(x, dataset):
    distance = getattr(distances, args.distance)

    neighbour = {}
    for d in dataset:
        dist = distance(x, d)
        elem = {'elem': d, 'distance': dist, 'class': d[len(d)-1]}
        if(neighbour == {} or dist < neighbour['distance']): neighbour = elem
    
    return neighbour
