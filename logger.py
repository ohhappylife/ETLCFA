import logging
from config import loglevel
# Logs will be stored on ETLlog.txt file
# Change the level to log with different level (ERROR, CRITICAL, DEBUG ...)
logger = logging

logger.basicConfig(filename='ETLlog.txt', # file name to store logs
                    format='%(levelname)s %(asctime)s :: %(message)s', # Format
                    level=logging.ERROR) # log level ~ ERROR, CRITICAL, DEBUG ...