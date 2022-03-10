import os

SRC_DIR = os.path.dirname(__file__)

PROJECT_DIR = os.path.dirname(SRC_DIR)

DATA_DIR = os.path.join(PROJECT_DIR, "../../data")
if not os.path.exists(DATA_DIR):
    os.mkdir(DATA_DIR)

LOG_DIR = os.path.join(PROJECT_DIR, "../../logs")
if not os.path.exists(LOG_DIR):
    os.mkdir(LOG_DIR)
LOG_ALL_PATH = os.path.join(LOG_DIR, "all.log")
LOG_ERR_PATH = os.path.join(LOG_DIR, "err.log")
