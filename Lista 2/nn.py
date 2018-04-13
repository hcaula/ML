# Module to return the nearest class from element
import distances
from args import args

def nn(x, k, dataset):
    distance = getattr(distances, args.distance)

    neighbours = []
    for i in range(k):
        neighbours.append({})

    for d in dataset:
        dist = distance(x, d)
        elem = {'elem': d, 'distance': dist, 'class': d[len(d)-1]}

        for n in range(len(neighbours)):
            neighbour = neighbours[n]
            if(neighbour == {} or dist < neighbour['distance']):
                neighbours[n] = elem
                n = len(neighbours)+1
    
    return neighbours
