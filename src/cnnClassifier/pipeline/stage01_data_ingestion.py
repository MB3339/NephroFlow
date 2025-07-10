from cnnClassifier.components import data_ingestion
from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.data_ingestion import DataIngestion
from cnnClassifier import logger

Stage_name = "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config_manager = ConfigurationManager()
        data_ingestion_config = config_manager.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.extract_zip_file()

if __name__ == "__main__":
    try:
        logger.info(f"{Stage_name} started")
        pipeline = DataIngestionTrainingPipeline()
        pipeline.main()
        logger.info(f"{Stage_name} completed successfully")
    except Exception as e:
        logger.exception(f"Error occurred in {Stage_name}: {e}")
        raise e