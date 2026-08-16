from pathlib import Path


BASE_DIR = Path(__file__).parent
DATA_DIR_NAME = "data"
CATEGORY_FILE_NAME = "categories.csv"

DATA_DIR = BASE_DIR / DATA_DIR_NAME
CATEGORY_STORAGE_PATH = DATA_DIR / CATEGORY_FILE_NAME

