from cnnClassifier.constants import *
from cnnClassifier.utils.common import read_yaml, create_directories 

from cnnClassifier.constants import CONFIG_FILE_PATH, PARAM_FILE_PATH
from cnnClassifier.utils.common import read_yaml, create_directories
from pathlib import Path
from cnnClassifier.entity.config_entity import DataIngestionConfig, PrepareBaseModelConfig

class ConfigurationManager:
    def __init__(self,
                 config_path: Path = CONFIG_FILE_PATH,
                 param_path: Path = PARAM_FILE_PATH):
        """
        Loads config and param YAML files, and sets up the artifacts root directory.
        """
        self.config = read_yaml(config_path)
        self.param = read_yaml(param_path)
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """
        Extracts data ingestion configuration from config.yaml and ensures directories exist.
        """
        config = self.config.data_ingestion
        create_directories([config.root_dir])

        return DataIngestionConfig(
            root_dir=config.root_dir,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        """
        Extracts base model preparation configuration from config.yaml and param.yaml.
        """
        config = self.config.prepare_base_model
        params = self.param.prepare_base_model # Assuming this is how your param.yaml is structured

        create_directories([config.root_dir])

        return PrepareBaseModelConfig(
            root_dir=config.root_dir,
            base_model_path=config.base_model_path,
            updated_base_model_path=config.updated_base_model_path,
            param_image_size=params.image_size,
            param_learning_rate=params.learning_rate,
            param_include_top=params.include_top,
            param_weights=params.weights,
            param_classes=params.classes
        )