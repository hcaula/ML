# Importing libs
import argparse
import arff

# Setting command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-k', required=True, type=int, help='The k value for the k-NN')
parser.add_argument('-w', action='store_true', help='If the distance should be weighted or not')
parser.add_argument('-datasets', nargs=2, required=True, help='The datasets arff files')
parser.add_argument('-distance', required=True, choices=['euclidean', 'vdm', 'hvdm'], help='The type of distance used for calculations')

args = parser.parse_args()

print args.distance