import arff

def read(filename):
    f = open(filename, 'rb')
    if ('.data' in filename): return parse_data(f)
    elif ('.arff' in filename): return arff.load(f)['data']
    else: raise Exception('This file is not supported. Please, choose either .arff or .data')

def parse_data(f):
    data = f.read()
    data = data.split('\n')
    big_data = []
    for d in data:
        big_data.append(d.split(','))
    return big_data