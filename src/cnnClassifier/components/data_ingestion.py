import os
import zipfile
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size 
from cnnClassifier.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        """
        Initializes the Data Ingestion class with the provided configuration.
        """
        self.config = config

    def extract_zip_file(self):
        """
        Extracts the ZIP file into the specified directory.
        """
        unzip_path = self.config.unzip_dir
        zip_file_path = self.config.local_data_file

        if not os.path.exists(zip_file_path):
            logger.error(f"ZIP file not found at {zip_file_path}")
            raise FileNotFoundError(f"{zip_file_path} does not exist")

        logger.info(f"Unzipping {zip_file_path} to {unzip_path}")
        os.makedirs(unzip_path, exist_ok=True)

        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)

        logger.info("Extraction completed.")