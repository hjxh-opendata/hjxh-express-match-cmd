import os

PROJECT_DIR = os.path.dirname(__file__)

DATA_DIR = os.path.join(PROJECT_DIR, "../data")
os.makedirs(DATA_DIR, exist_ok=True)

LOG_DIR = os.path.join(PROJECT_DIR, "../logs")
os.makedirs(LOG_DIR, exist_ok=True)
