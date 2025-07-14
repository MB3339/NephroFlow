# import os
# import urllib.request as request
# from zipfile import ZipFile
# import tensorflow as tf
# import time
# from cnnClassifier.entity.config_entity import TrainingConfig
# from pathlib import Path
# from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau


# class Training:
#     def __init__(self,config:TrainingConfig):
#         self.config = config

#     def get_base_model(self):
#         self.model = tf.keras.models.load_model(
#             self.config.updated_model_path
#         )
#     def train_valid_generator(self):

#         datagenerator_Kwargs = dict(
#             rescale=1./255,
#             validation_split=0.2    
#         )

#         dataflow_kwargs = dict(
#             target_size=self.config.params_image_size[:-1],
#             batch_size=self.config.params_batch_size,
#             interpolation="bilinear"
#         )

#         validation_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
#             ** datagenerator_Kwargs
#         )

#         self.valid_generator = validation_datagenerator.flow_from_directory(
#             directory=self.config.training_data,
#             subset="validation",
#             shuffle=False,
#             **dataflow_kwargs
#         )

#         if self.config.params_is_augmentation:
#             train_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
#                 rotation_range=40,
#                 width_shift_range=0.2,
#                 height_shift_range=0.2,
#                 shear_range=0.2,
#                 zoom_range=0.2,
#                 horizontal_flip=True,
#                 fill_mode="nearest",
#                 **datagenerator_Kwargs
#             )
#         else:
#             train_datagenerator=validation_datagenerator
        
#         self.train_generator = train_datagenerator.flow_from_directory(
#             directory=self.config.training_data,
#             subset="training",
#             shuffle=True,
#             **dataflow_kwargs
#         )

#     @staticmethod
#     def save_model(path:Path, model:tf.keras.Model):
#         model.save(path)
#         print(f"Model saved at {path}")


#     def train(self):
#         early_stop = EarlyStopping(
#             monitor='val_loss',
#             patience=5,
#             restore_best_weights=True
#         )

#         lr_scheduler = ReduceLROnPlateau(
#             monitor='val_loss',
#             factor=0.2,
#             patience=3,
#             min_lr=1e-6
#         )


#     def train(self,callback_list: list):
#         self.steps_per_epoch=self.train_generator.samples // self.config.params_batch_size
#         self.validation_steps=self.valid_generator.samples // self.valid_generator.batch_size

#         self.model.fit(
#             self.train_generator,
#             steps_per_epoch=self.steps_per_epoch,
#             validation_data=self.valid_generator,
#             validation_steps=self.validation_steps,
#             epochs=self.config.params_epochs,
#             callbacks=[early_stop, lr_scheduler] # making earlystop if needed
#         )

#         self.save_model(
#             self.config.training.trained_model_path, 
#             self.model
#             )

        
import os
import tensorflow as tf
from pathlib import Path
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau
from cnnClassifier.entity.config_entity import TrainingConfig
import urllib.request as request
from zipfile import ZipFile
import time

class Training:
    def __init__(self, config: TrainingConfig):
        self.config = config

    def get_base_model(self):
        self.model = tf.keras.models.load_model(
            self.config.updated_model_path
        )

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

        validation_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_Kwargs
        )

        self.valid_generator = validation_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="validation",
            shuffle=False,
            **dataflow_kwargs
        )

        if self.config.params_is_augmentation:
            train_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
                rotation_range=40,
                width_shift_range=0.2,
                height_shift_range=0.2,
                shear_range=0.2,
                zoom_range=0.2,
                horizontal_flip=True,
                fill_mode="nearest",
                **datagenerator_Kwargs
            )
        else:
            train_datagenerator = validation_datagenerator
        
        self.train_generator = train_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="training",
            shuffle=True,
            **dataflow_kwargs
        )

    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)
        print(f"Model saved at {path}")

    def train(self):
        early_stop = EarlyStopping(
            monitor='val_loss',
            patience=5,
            restore_best_weights=True
        )

        lr_scheduler = ReduceLROnPlateau(
            monitor='val_loss',
            factor=0.2,
            patience=3,
            min_lr=1e-6
        )

        self.steps_per_epoch = self.train_generator.samples // self.config.params_batch_size
        self.validation_steps = self.valid_generator.samples // self.valid_generator.batch_size

        self.model.fit(
            self.train_generator,
            steps_per_epoch=self.steps_per_epoch,
            validation_data=self.valid_generator,
            validation_steps=self.validation_steps,
            epochs=self.config.params_epochs,
            callbacks=[early_stop, lr_scheduler]
        )

        self.save_model(
            self.config.trained_model_path, 
            self.model
        )

        