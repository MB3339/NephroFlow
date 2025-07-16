import tensorflow as tf
import numpy as np
import os
from tensorflow.keras.preprocessing import image

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename
        self.model = tf.keras.models.load_model(os.path.join("model", "trained_model.h5"))

    def predict(self):
        img = image.load_img(self.filename, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0) / 255.0

        prediction = self.model.predict(img_array)

        class_idx = np.argmax(prediction, axis=1)[0]
        class_labels = {0: "Normal", 1: "Tumor"}

        return class_labels[class_idx]
