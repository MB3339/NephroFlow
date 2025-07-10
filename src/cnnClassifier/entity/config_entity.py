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