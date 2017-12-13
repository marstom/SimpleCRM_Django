'''
logging events and user activities
'''

import logging

formatter = logging.Formatter('%(asctime)s %(levelname)s: \t %(message)s')


def setup_logger(name, log_file, level, console=False):
    """Function setup as many loggers as you want"""

    if not console:
        handler = logging.FileHandler(log_file)
    else:
        handler = logging.StreamHandler()

    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger


# file logging for debug burposes
logger = setup_logger('debug_logger', 'mycrm_info_and_debug.log', logging.INFO)

# logger for user tracking, it log info about users activities
logger_user_activity = setup_logger('user_activity', 'mycrm_user_activity.log', logging.INFO)
