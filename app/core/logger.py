import logging

from .config import settings


def _initialize_logger(
    log_name: str,
    log_level: str,
    add_console_handler: bool = True,
    add_file_handler: bool = False,
    log_file_path: str = None,
) -> logging.Logger:
    """
    Initialize a logger with the specified configuration.

    Args:
        log_name (str): The name of the logger.
        log_level (str): The log level for the logger.
        add_console_handler (bool, optional): Whether to add a console handler to the logger. Defaults to True.
        add_file_handler (bool, optional): Whether to add a file handler to the logger. Defaults to False.
        log_file_path (str, optional): The file path for the log file. Required if add_file_handler is True.

    Returns:
        logging.Logger: The initialized logger.
    """
    logger = logging.getLogger(log_name)
    logger.setLevel(log_level)

    if add_console_handler:
        ch = logging.StreamHandler()
        ch.setLevel(log_level)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        ch.setFormatter(formatter)
        logger.addHandler(ch)

    if add_file_handler:
        fh = logging.RotatingFileHandler(
            log_file_path, maxBytes=10000000, backupCount=5
        )
        fh.setLevel(log_level)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    return logger


logger = _initialize_logger(
    log_name=settings.PROJECT_NAME,
    log_level=settings.LOG_LEVEL,
    add_console_handler=settings.LOG_ADD_CONSOLE_HANDLER,
    add_file_handler=settings.LOG_ADD_FILE_HANDLER,
    log_file_path=settings.LOG_FILE_PATH,
)
