import datetime
import logging.handlers

from .paths import LOG_ALL_PATH, LOG_ERR_PATH

logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)

rf_handler = logging.handlers.TimedRotatingFileHandler(
    LOG_ALL_PATH, when='midnight', interval=1, backupCount=7, atTime=datetime.time(0, 0, 0, 0))
rf_handler.setFormatter(logging.Formatter(
    "%(asctime)s - %(levelname)s - %(funcName)s - %(message)s"))

f_handler = logging.FileHandler(LOG_ERR_PATH)
f_handler.setLevel(logging.ERROR)
f_handler.setFormatter(logging.Formatter(
    "%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(funcName)s - %(message)s"))

logger.addHandler(rf_handler)
logger.addHandler(f_handler)

# logger.debug('debug message')
# logger.info('info message')
# logger.warning('warning message')
# logger.error('error message')
# logger.critical('critical message')
