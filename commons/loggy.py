import logging
import logging.handlers
import os
from datetime import datetime
import sys
import errno
# Logging Levels
# https://docs.python.org/3/library/logging.html#logging-levels
# CRITICAL  50
# ERROR 40
# WARNING   30
# INFO  20
# DEBUG 10
# NOTSET 0


def set_up_logging(name=None):
    file_path = sys.modules[__name__].__file__
    project_path = os.path.dirname(os.path.dirname(file_path))
    log_location = project_path + '/logs/'

    if not os.path.exists(log_location):
        try:
            os.makedirs(log_location, exist_ok=True)
        except TypeError:
            try:
                os.makedirs(log_location)
            except OSError as exc:  # Python >2.5
                if exc.errno == errno.EEXIST and os.path.isdir(log_location):
                    pass
                else:
                    raise

    current_time = datetime.now()
    current_date = current_time.strftime("%Y%m%d")
    #file_name = current_date + '.log'
    file_name = 'zybots_' + current_date + '.log'
    file_location = log_location + file_name
    with open(file_location, 'a+'):
        pass
    if name:
        logger = logging.getLogger(name)
    else:
        logger = logging.getLogger(__name__)
    format = '[%(asctime)s] [%(levelname)s] [%(message)s] [%(pathname)s %(name)s [%(process)d]:]'
    # To store in file
    logging.basicConfig(format=format, filemode='a+', filename=file_location, level=logging.DEBUG)
    # To print only
    #logging.basicConfig(format=format, level=logging.DEBUG)
    return logger
