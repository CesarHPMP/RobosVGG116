from keras_applications import vgg16
from keras_applications.vgg16 import VGG16
from keras_preprocessing.image import load_img
from keras_preprocessing import image
from keras_applications.imagenet_utils import preprocess_input
import numpy as np

image = load_img('./data/teste.jpeg', target_size=(224, 224))

image = np.array(image)

image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))

image = preprocess_input(image)

my_image = imread('./data/teste.jpeg')