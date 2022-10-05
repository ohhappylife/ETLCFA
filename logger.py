import logging
# Logs will be stored on ETLlog.txt file
# Change the level to log with different levle (ERROR, CRITICAL, DEBUG ...)
logger = logging

logger.basicConfig(filename='ETLlog.txt',
                    format='%(levelname)s %(asctime)s :: %(message)s',
                    level=logging.ERROR)