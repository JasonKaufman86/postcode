import logging
import pathlib
from typing import Optional


from . import PACKAGE_NAME, PACKAGE_VERSION


from logging.handlers import RotatingFileHandler

logger = logging.getLogger(f"{PACKAGE_NAME}-{PACKAGE_VERSION}")
logger.addHandler(logging.NullHandler())  # Avoid "No handlers could be found" warning


def configure_logger(
    level: str = "INFO",
    to_console: bool = True,
    to_file: Optional[str] = None,
) -> None:
    """
    Configure the internal logger for the postcode package.

    Args:
        level (str): Logging level, e.g. 'INFO', 'DEBUG', 'WARNING'.
        to_console (bool): Whether to output logs to the console.
        to_file (Optional[str]): File path to log to. If None, file logging is disabled.
    """
    logger.setLevel(level.upper())
    logger.handlers.clear()

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    if to_console:
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        stream_handler.setLevel(level)
        logger.addHandler(stream_handler)

    if to_file:
        log_path = pathlib.Path(to_file)
        log_path.parent.mkdir(parents=True, exist_ok=True)
        file_handler = RotatingFileHandler(log_path, maxBytes=10 * 1024 * 1024, backupCount=3)
        file_handler.setFormatter(formatter)
        file_handler.setLevel(level)
        logger.addHandler(file_handler)
