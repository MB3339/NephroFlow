import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from pathlib import Path

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename
        self.model_path = Path("artifacts/training/trained_model.h5")

    def predict(self):
        # Load the trained model
        model = tf.keras.models.load_model(self.model_path)

        # Preprocess the input image
        img = image.load_img(self.filename, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0) / 255.0  # Normalize

        # Make prediction
        prediction = model.predict(img_array)

        # Assuming binary classification: 0=Normal, 1=Tumor
        class_idx = np.argmax(prediction, axis=1)[0]
        class_labels = {0: "Normal", 1: "Tumor"}

        return class_labels[class_idx]