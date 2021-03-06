import argparse

def limit_split(split):
    split = float(split)
    if split < 0: raise argparse.ArgumentTypeError("Minimum split value is 0")
    elif split > 1: raise argparse.ArgumentTypeError("Maximum split value is 1")
    return split

# Setting command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-d', default="datasets/cm1.arff", help='The dataset file in .arff')
parser.add_argument('-k', default=2, type=int, help='The k value for the k-NN')
parser.add_argument('-p', default=1, type=int, help='The number of prototypes per class of the dataset')
parser.add_argument('-r', default=1, type=int, help='The number of repetions for each LVQ')
parser.add_argument('-window', default=0.6, type=limit_split, help='The weight for the window rule')
parser.add_argument('-split', default=0.66, type=limit_split, help='The percentage for the training set')
parser.add_argument('-repetitions', default=1, type=int, help="How many times should we run ALL LVQ's")
parser.add_argument('-w', action='store_true', help='If the distance should be weighted or not')
parser.add_argument('-distance', default='euclidean', choices=['euclidean', 'vdm', 'hvdm'], help='The type of distance used for calculations')
parser.add_argument('-prototype', default='limited', choices=['limited'], help='The way the first prototypes should be generated')
parser.add_argument('-shuffle', action='store_true', help='If the dataset should be randomly shuffled before k-fold')
parser.add_argument('-swap', action='store_true', help='If the class attribute is on the first spot')

args = parser.parse_args()