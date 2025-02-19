import logging
import os

logging.basicConfig(datefmt='%Y-%m-%d %H:%M:%S', \
    format='%(asctime)s %(levelname)-8s %(message)s', \
    level=os.environ.get("LOGLEVEL"))