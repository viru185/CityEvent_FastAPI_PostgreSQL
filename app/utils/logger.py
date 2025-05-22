import os
from loguru import logger

from app.config import (
    LOGS_FILE,
    LOGS_DIR,
    LOG_LEVEL,
    LOG_TO_FILE,
    LOG_TO_CONSOLE,
)

# Ensure logs directory exists
os.makedirs(LOGS_DIR, exist_ok=True)


def init_loguru():

    # Remove the default logger
    logger.remove()

    # Add file logger if LOG_TO_FILE is True
    if LOG_TO_FILE:
        logger.add(
            LOGS_FILE,
            level=LOG_LEVEL,
            rotation="10 MB",
            retention="1 week",
            compression="zip",
        )

    # Add console logger if LOG_TO_CONSOLE is True
    if LOG_TO_CONSOLE:
        logger.add(
            os.sys.stdout,
            level=LOG_LEVEL,
            colorize=True,
        )


init_loguru()
