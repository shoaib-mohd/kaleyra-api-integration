# -*- coding: utf-8 -*-
import logging

logFormatter = logging.Formatter(
    fmt="[%(asctime)s.%(msecs)03d] [%(name)s: %(levelno)s] [%(funcName)s: %(lineno)d]  %(message)s\n",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger("main")
logging.getLogger("boto3").setLevel(logging.CRITICAL)
logging.getLogger("werkzeug").setLevel(logging.ERROR)

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
logger.addHandler(consoleHandler)

logger.setLevel(logging.INFO)
