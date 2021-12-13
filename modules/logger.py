import os
import logging
import logging.handlers as handlers


def log_generate():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    logfile_directory = os.path.join(current_dir, "logs")
    if not os.path.exists(logfile_directory):
        os.mkdir(logfile_directory)

    logfile_name = "test.log"
    logfile_path = os.path.join(logfile_directory, logfile_name)

    global logger
    logger = logging.getLogger("app")
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s")
    logHandler = handlers.TimedRotatingFileHandler(
        logfile_path, when="midnight", interval=1, backupCount=0)
    logHandler.setLevel(logging.INFO)
    logHandler.setFormatter(formatter)
    logger.addHandler(logHandler)
    logger.info("Initailize logging")
    return logger

logger = log_generate()