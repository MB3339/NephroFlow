from cnnClassifier.constants import *
from cnnClassifier.utils.common import read_yaml, create_directories 

from cnnClassifier.constants import CONFIG_FILE_PATH, PARAM_FILE_PATH
from cnnClassifier.utils.common import read_yaml, create_directories
from pathlib import Path
from cnnClassifier.entity.config_entity import DataIngestionConfig

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
    