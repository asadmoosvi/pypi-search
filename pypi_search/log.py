import logging, sys


def init_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler(sys.stderr)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('[%(levelname)s] :: %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
