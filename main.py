from cnnClassifier import logger
from cnnClassifier.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline

Stage_name = "Data Ingestion stage"
if __name__ == "__main__":
    try:
        logger.info(f"{Stage_name} started")
        pipeline = DataIngestionTrainingPipeline()
        pipeline.main()
        logger.info(f"{Stage_name} completed successfully")
    except Exception as e:
        logger.exception(f"Error occurred in {Stage_name}: {e}")
        raise e