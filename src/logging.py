import logging
import os


def get_logger(path):
    """Creates a logger

    :param path: path of log
    :return:
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)
    logger = logging.getLogger()
    fhandler = logging.FileHandler(filename=path, mode='a')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fhandler.setFormatter(formatter)
    logger.addHandler(fhandler)
    logger.setLevel(logging.DEBUG)

    return logger