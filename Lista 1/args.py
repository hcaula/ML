import argparse

# Setting command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-d', required=True, help='The dataset file in .arff')
parser.add_argument('-k', default=2, type=int, help='The k value for the k-NN')
parser.add_argument('-w', action='store_true', help='If the distance should be weighted or not')
parser.add_argument('-distance', default='euclidean', choices=['euclidean', 'vdm', 'hvdm'], help='The type of distance used for calculations')
parser.add_argument('-kfold', type=int, default=5, help='The k value for the k-fold cross-validation')
parser.add_argument('-shuffle', action='store_true', help='If the dataset should be randomly shuffled before k-fold')

args = parser.parse_args()