from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    """
    Data Ingestion Configuration for the Kidney Disease Classification Project.
    Now adapted for local ZIP ingestion only.
    """
    root_dir: Path
    local_data_file: Path  # Path to the local ZIP file
    unzip_dir: Path        # Destination directory for extracted contents


@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path 
    base_model_path: Path
    updated_base_model_path: Path
    param_image_size: list 
    param_learning_rate: float
    param_include_top: bool
    param_weights: str
    param_classes: int


@dataclass(frozen=True)
class TrainingConfig:
    root_dir: Path
    trained_model_path: Path
    updated_model_path: Path
    training_data: Path
    params_epochs: int
    params_batch_size: int
    params_is_augmentation: bool
    params_image_size: list
