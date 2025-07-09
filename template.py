import os
from pathlib import Path
import logging

# Logging Strings
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:  %(message)s:')

project_name = "cnnClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f" src/ {project_name}/__init__.py",
    f" src/ {project_name}/components/__init__.py",
    f" src/ {project_name}/utils/__init__.py",
    f" src/ {project_name}/config/__init__.py",
    f" src/ {project_name}/config/configuration.py",
    f" src/ {project_name}/pipeline/__init__.py",
    f" src/ {project_name}/entity/__init__.py",
    f" src/ {project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
]

for file in list_of_files:
    file_path = Path(file)
    filedir,filename = os.path.split(file_path)

    if filedir!="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating file: {file} for the file name {filename}")
    
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, 'w') as f:
            pass
        logging.info(f"Creating file: {file}")
        # Ensure the directory exists before creating the file
    else:
        logging.info(f"File already exists: {file}")