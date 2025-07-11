import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
from pathlib import Path
from cnnClassifier.config.configuration import PrepareBaseModelConfig

class PrepareBaseModel:
    def __init__(self, config: PrepareBaseModelConfig):
        self.config = config

    def get_base_model(self):
        self.base_model = tf.keras.applications.VGG16(
            input_shape=self.config.param_image_size,
            include_top=self.config.param_include_top,
            weights=self.config.param_weights,
            classes=self.config.param_classes
        )
        self.save_base_model(path=self.config.base_model_path,model=self.base_model)

    @staticmethod
    def prepare_full_base_model(model,classes, freeze_all, freeze_till, learning_rate):
        """
        Prepares the base model by freezing layers and compiling it.
        """
        if freeze_all:
            for layer in model.layers:
                model.trainable = False
        elif freeze_till is not None and (freeze_till > 0):
            for layer in model.layers[:- freeze_till]:
                model.trainable = False
        flatten_in= tf.keras.layers.Flatten()(model.output)
        prediction= tf.keras.layers.Dense(
            units=classes,
            activation="softmax"
        )(flatten_in)
        
        full_model= tf.keras.models.Model(
            inputs=model.input,
            outputs=prediction
        )

        full_model.compile(
            optimizer= tf.keras.optimizers.SGD(learning_rate=learning_rate),
            loss=tf.keras.losses.CategoricalCrossentropy(),
            metrics=['accuracy']
        )
        full_model.summary()
        return full_model

    def update_base_model(self):
        self.prepared_base_model = self.prepare_full_base_model(
            model=self.base_model,
            classes=self.config.param_classes,
            freeze_all=True,
            freeze_till=None,
            learning_rate=self.config.param_learning_rate
        )
        self.save_base_model(path=self.config.updated_base_model_path, model=self.prepared_base_model)

    @staticmethod
    def save_base_model(path: Path, model: tf.keras.Model):
        """
        Saves the base model to the specified path.
        """
        model.save(path)
        print(f"Base model saved at {path}")