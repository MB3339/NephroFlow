from cnnClassifier import logger
from cnnClassifier.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage02_prepare_base_model import PrepareBaseModelTrainingPipeline

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
    
Stage_Name = "02_prepare_base_model"
if __name__ == "__main__":
    try:
        logger.info(f">>>>> stage {Stage_Name} started <<<<<")
        prepare_base_model_pipeline = PrepareBaseModelTrainingPipeline()
        prepare_base_model_pipeline.main()
        logger.info(f">>>>> stage {Stage_Name} completed <<<<<")
    except Exception as e:
        logger.exception(e)
        raise e 