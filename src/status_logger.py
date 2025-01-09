import logging
logging.basicConfig(
    filename='history_status.log',
    filemode='a',
    format='%(asctime)s, %(msecs)d %(name)s - %(levelname)s : %(message)s',
    datefmt='%H:%M:%S',
    level=logging.DEBUG  
)

level_map = {
    'debug': logging.debug,
    'info': logging.info,
    'warning': logging.warning,
    'error': logging.error,
    'critical': logging.critical,
}
def debug_logger(level_name,message):

        log_func = level_map[level_name.lower()]
        if log_func:
            log_func(message)
        else:
            logging.error(f"Invalid logging level: {level_name}")