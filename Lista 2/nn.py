# Module to return the nearest class from element
import distances
from args import args

def nn(x, k, dataset):
    distance = getattr(distances, args.distance)

    neighbours = []
    for d in dataset:
        dist = distance(x, d)
        elem = {'distance': dist, 'class': d[len(d)-1]}

        # If the list of neighbours hasn't reached its limit, add to the list
        if(len(neighbours) < k): neighbours.append(elem)
        else:
            max_neighbour = max(neighbours, key=lambda x: x['distance'])

            # If the furthest neighbour is further than the new element, swap them
            if(dist < max_neighbour['distance']): 
                index = neighbours.index(max_neighbour)
                neighbours[index] = elem
    
    # Counts the number of classes for the k-nearests neighbours
    classes = {}
    for n in neighbours:
        if(n['class'] in classes): classes[n['class']] += 1
        else: classes[n['class']] = 1
    
    # Sets the prediction to be the class with most neighbours
    prediction = max(classes, key=classes.get)
    return prediction
