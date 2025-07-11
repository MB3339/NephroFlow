from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.prepare_base_model import PrepareBaseModel
from cnnClassifier import logger


Stage_Name = "02_prepare_base_model"

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        # Step 1: Load the config
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()

        # Step 2: Prepare the base model
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()


if __name__ == "__main__":
    try:
        logger.info(f">>>>> stage {Stage_Name} started <<<<<")
        prepare_base_model_pipeline = PrepareBaseModelTrainingPipeline()
        prepare_base_model_pipeline.main()
        logger.info(f">>>>> stage {Stage_Name} completed <<<<<")
    except Exception as e:
        logger.exception(e)
        raise e