import tensorflow as tf
from PIL import Image

im = Image.open(open("test.jpg"))

nn = tf.image.decode_jpeg("test", channels=3)

print nn.get_shape()
