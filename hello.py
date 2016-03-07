import numpy as np
import cPickle
import os
import time

def unpick():
    file_open = os.path.join('cifar-10-batches-py', 'data_batch_1')
    f = open(file_open, 'rb')

    images = cPickle.load(f)

    print len(images)

    for i in len(images):
        print images[i]
    f.close()
   # print(images)
    return images

if __name__ == '__main__':

    # print "hello"
    images = unpick()
