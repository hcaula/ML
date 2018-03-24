import sys, os
import arff

k = int(sys.argv[1])
w = sys.argv[2] in ["weighted", "w", "true"]
distance = sys.argv[3]
datasets = [sys.argv[4], sys.argv[5]]

data = arff.load(open('datasets/cm1.arff', 'rb'))

print data