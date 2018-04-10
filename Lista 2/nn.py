# Module to return the nearest class from element
import distances
from args import args

def nn(x, dataset):
    distance = getattr(distances, args.distance)

    neighbour = {}
    for d in dataset:
        dist = distance(x, d)
        elem = {'data': d, 'distance': dist}
        if(neighbour == {} or dist < neighbour['distance']): neighbour = elem
    
    return neighbour
