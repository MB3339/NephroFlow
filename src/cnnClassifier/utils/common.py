import os 
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import  ConfigBox
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """read a yaml file and return 
    Args:
        path_to_yaml (Path): path to the yaml file
    
    Raises:
        ValueError: if the file does not exist or is empty
        e: empty file
        
    Returns:    
        ConfigBox: ConfigBox object containing the yaml file content
    """
    try:
        with open(path_to_yaml) as file:
            content = yaml.safe_load(file)
            logger.info(f"YAML file loaded successfully from {path_to_yaml}")
            return ConfigBox(content)
    except BoxValueError as e:
        raise ValueError("The YAML file is empty") 
    except Exception as e:
        raise ValueError(f"Error reading the YAML file: {e}")
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose = True) :
    """Create list of directories.
    
    Args:
        path_to_directories (list):list of Path of the directories.
        ignore log(bool,optional): Ignore if multiple dirs are to be created.

    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory: {path}")
        
@ensure_annotations
def save_json(path: Path, data: dict):
    """Save JSON Data.
    
    Args:
        path (Path): Path to the JSON file.
        data (dict): Data to be saved in Json File.
    """
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)
    logger.info(f"JSON file saved at {path}")

@ensure_annotations

def save_bin(data: Any, path: Path):
    """Save data in binary format.
    
    Args:
        data (Any): Data to be saved.
        path (Path): Path to the binary file.
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved at {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """Load data from binary file.
    
    Args:
        path (Path): Path to the binary file.
    
    Returns:
        Any: Data loaded from the binary file.
    """
    data = joblib.load(path)
    logger.info(f"Binary file loaded from {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """Get the size of a file.
    
    Args:
        path (Path): Path to the file.
    
    Returns:
        str: Size of the file in KiloBytes.
    """
    size = os.path.getsize(path) / 1024
    logger.info(f"Size of the file {path} is {size} KiloBytes")
    return f"{size} KiloBytes"


def decodeImage(imstring,filename) :
    imgdata= base64.b64decode(imstring)
    with open(filename,'wb') as f:
        f.write(imgdata)    
        f.close()

def encodeImageIntoBase64(croppedImagepath):
    with open(croppedImagepath,'rb') as f:
        return base64.b64encode(f.read())
    