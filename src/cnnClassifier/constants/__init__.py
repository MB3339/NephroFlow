# from pathlib import Path

# CONFIG_FILE_PATH = Path("config/config.yaml")
# PARAM_FILE_PATH = Path("param.yaml")

from pathlib import Path

# Go up 3 levels from src/cnnClassifier/constants to reach project root
ROOT_DIR = Path(__file__).resolve().parents[3]

CONFIG_FILE_PATH = ROOT_DIR / "config" / "config.yaml"
PARAM_FILE_PATH = ROOT_DIR / "param.yaml"
