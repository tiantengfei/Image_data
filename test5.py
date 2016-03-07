import cPickle
import numpy as np
import os

def read():
    f = os.path.join("cifar-10-batches-py", "data_batch_1")
    fo = open(f, 'rb')
    image = cPickle.load(fo)

    data = image['data']
    labels = image['labels']

    print data.shape
    print labels[2]

if __name__ == '__main__':
    read()
