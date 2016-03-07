import numpy as np
from PIL import Image
import sys
import tensorflow as tf

def saveImage():
    im = Image.open("test.jpg")
    m1 = np.array(im)
    m2 = np.array(im)
    m1 = np.transpose(m1, (1, 0, 2))
    m2 = np.transpose(m2, (1, 0, 2))
    print m1.shape, m2.shape
    m3 = np.concatenate((m1, m2), axis=2)

   # print m3.shape
    f = open("image.bin", "wb")
    f.write('1')
    f.write(m3.tostring())
    f.write('1')
    f.write(m3.tostring())
    print sys.getsizeof(m3.tostring())

   # a = np.array([[1, 2], [3, 4]])
   # f.write(a.tostring() + "\n")

    f.close()

def readImage():

    f = open("image.bin", "rb")

    #im = f.read()
   # im=np.fromstring(im, dtype=np.uint8).reshape(160, 160, 6)

   # print im.shape
    while True:
        print  f.read(1)
        im = f.read(153600)
        if im == '':
            break
        im = np.fromstring(im, dtype=np.uint8).reshape(160, 160, 6)

        print im.shape


   # print im.shape
    #with open("image.bin", "rb") as f:

      #  for line in f:

         #   im = line #if line[-1] == "\n" else line
        #    im = np.fromstring(im, dtype=np.uint8).reshape(160, 160, 6)
        #    print im.shape

if __name__ == "__main__":
    saveImage()
    readImage()