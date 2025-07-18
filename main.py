from cnnClassifier import logger
from cnnClassifier.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_model_training import ModelTrainingPipeline
from cnnClassifier.pipeline.Stage_04_model_evaluation import ModelEvaluationPipeline

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
    
Stage_name = "Model Training stage"
if __name__=='__main__':
    try:
        logger.info(f">>>>> Stage {Stage_name} started <<<<<")
        model_training = ModelTrainingPipeline()
        model_training.main()
        logger.info(f">>>>> Stage {Stage_name} completed <<<<<\n\n")
    except Exception as e:
        logger.exception(f"Error occurred in {Stage_name}: {e}")
        raise e
    
Stage_Name = "Model_Evaluation_Stage"
if __name__=='__main__':
    try:
        logger.info(f">>>>> Stage {Stage_name} started <<<<<")
        model_training = ModelEvaluationPipeline()
        model_training.main()
        logger.info(f">>>>> Stage {Stage_name} completed <<<<<\n\n")
    except Exception as e:
        logger.exception(f"Error occurred in {Stage_name}: {e}")
        raise e
    