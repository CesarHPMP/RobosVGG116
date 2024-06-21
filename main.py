from keras_preprocessing.image import load_img
from keras_preprocessing import image
# AttributeError: 'NoneType' object has no attribute 'image_data_format'
import numpy as np
import keras
from tf_keras.applications.imagenet_utils import preprocess_input


image = load_img('data/teste.jpeg', target_size=(224, 224))

image = np.array(image)

image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))

image = preprocess_input(image)