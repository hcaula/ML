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

        count = 0
        for n in neighbours:
            if(n == {} or dist < n['distance']):
                neighbours[count] = elem
                break
            count += 1
    
    return neighbours
