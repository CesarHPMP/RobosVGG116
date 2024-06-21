from cv2 import WINDOW_AUTOSIZE, destroyAllWindows, imread, imshow, namedWindow, waitKey
from keras_preprocessing.image import load_img
from keras_preprocessing import image
import numpy as np
from tf_keras.applications.imagenet_utils import preprocess_input


image = load_img('data/teste.jpeg', target_size=(224, 224))

image = np.array(image)

image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))

image = preprocess_input(image)

namedWindow("show", WINDOW_AUTOSIZE)

my_img = imread('data/teste.jpeg')
imshow('show', my_img)

waitKey(0)
destroyAllWindows()