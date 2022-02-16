import datetime
import logging
import logging.handlers
import os

from base import LOG_DIR

LOG_ALL_PATH = os.path.join(LOG_DIR, "all.log")
LOG_ERR_PATH = os.path.join(LOG_DIR, "err.log")

my_logger = logging.getLogger('mylogger')
my_logger.setLevel(logging.DEBUG)

rf_handler = logging.handlers.TimedRotatingFileHandler(
    LOG_ALL_PATH, when='midnight', interval=1, backupCount=7, atTime=datetime.time(0, 0, 0, 0))
rf_handler.setFormatter(logging.Formatter(
    "%(asctime)s - %(levelname)s - %(funcName)s - %(message)s"))

f_handler = logging.FileHandler(LOG_ERR_PATH)
f_handler.setLevel(logging.ERROR)
f_handler.setFormatter(logging.Formatter(
    "%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(funcName)s - %(message)s"))

my_logger.addHandler(rf_handler)
my_logger.addHandler(f_handler)

# logger.debug('debug message')
# logger.info('info message')
# logger.warning('warning message')
# logger.error('error message')
# logger.critical('critical message')
