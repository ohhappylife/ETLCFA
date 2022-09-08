import logging

logger = logging

logger.basicConfig(filename='ETLlog.txt',
                    format='%(levelname)s %(asctime)s :: %(message)s',
                    level=logging.ERROR)