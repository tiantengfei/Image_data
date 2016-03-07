import pickle
from PIL import Image
import numpy as np

def save():
    favor_color = {"lion": "yellow", "kitty": "red"}
    pickle.dump(favor_color, open("save.p", "wb"))

def unpickle():
    favor_color = pickle.load(open("image.p", "rb"))
    arr = np.array(favor_color)
    print arr[2, 4, 5]

def image():
    im = Image.open("test2.jpg")
    #im = im.convert("rgb")
   # r, g, b = im.getpixel((80,89))
    m1 = np.array(im)
    m2 = np.array(im)
    m1 = np.transpose(m1, (1, 0, 2))
    m2 = np.transpose(m2, (1, 0, 2))
    print m1.shape, m2.shape

    m3 = np.concatenate((m1, m2), axis=2)

    print m3.dtype
    #print m3.tobytes()

    f = open("image.txt", "wb")
   # f.write(m3.tobytes())
    np.save(f, m3)

    m2 = np.array([[1, 2], [1, 2]])
    np.save(f, m2)
    #print str(m3)
    f.close()

    #pickle.dump((r, g, b), open("image.p", "wb"))
    #pickle.dump((r, g, b), open("image.p", "wb"))

    #print im.size
   # print r.shape, g.shape, b.shape


   # print(b)
def opImage():
    im = Image.open('test.jpg')
    #l = str(im)
    print im.tobytes()
    r, g, b = im.split()
    print list(r)
   # print list(im.getdata())
    image = im.convert("L")
    image.save("ratote.jpg", "jpeg")

def readImage():
    f = open("image.txt", "rb")
    #im_str = f.read()
    #im = np.array(im_str)
   # im = np.fromstring(im_str)
    im = np.load(f)
    im = np.reshape(im, (160,159, 6))
    im2 = np.load(f)
    print im.shape
    print im2.shape
   # print str(im)
if __name__ == '__main__':
   # unpickle()
    #image()
    image()

    readImage()
