import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
import mlflow
import mlflow.keras
from urllib.parse import urlparse
from cnnClassifier.entity.config_entity import EvaluationConfig
from cnnClassifier.utils.common import save_json
from pathlib import Path

class Evaluation:
    def __init__(self,config:EvaluationConfig):
        self.config = config


    def train_valid_generator(self):

        datagenerator_Kwargs = dict(
            rescale=1./255,
            validation_split=0.2    
        )

        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation="bilinear"
        )

        validation_generator = tf.keras.preprocessing.image.ImageDataGenerator(
            ** datagenerator_Kwargs
        )

        self.valid_generator = validation_generator.flow_from_directory(
            directory=self.config.training_data,
            subset="validation",
            shuffle=False,
            **dataflow_kwargs
        )

    @staticmethod
    def load_model(path: Path) -> tf.keras.Model:
        return tf.keras.models.load_model(path)

    def evaluation(self):
        self.model = self.load_model(self.config.path_of_model)
        self.train_valid_generator()
        loss, accuracy = self.model.evaluate(self.valid_generator)
        print(f"Model Evaluation -> Loss: {loss}, Accuracy: {accuracy}")

        # Save scores locally
        self.save_score(loss, accuracy)

        # Log metrics to MLflow/DagsHub
        mlflow.set_tracking_uri(self.config.mlflow_uri)
        with mlflow.start_run():
            mlflow.log_params(self.config.all_params)
            mlflow.log_metric("loss", loss)
            mlflow.log_metric("accuracy", accuracy)

    def save_score(self, loss, accuracy):
        scores = {"loss": loss, "accuracy": accuracy}
        save_json(path=Path('scores.json'), data=scores)