"""
Perdaryti 2 užduoties programą, kad:
    * Būtų sukurtas savo logeris, kuris fikstuotus
        visus anksčiau aprašytus pranešimus
    * Sukurtas logeris ne tik išsaugotų pranešimus
        faile, bet ir atvaizduotų juos konsolėje
"""

import math
from logging import FileHandler, StreamHandler, Formatter, getLogger, DEBUG

logger = getLogger("my_logger")
logger.setLevel(DEBUG)
formatter = Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler = FileHandler("logeris_12_3.log")
file_handler.setFormatter(formatter)
stream_handler = StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
logger.addHandler(file_handler)

logger.info('<Warning message.>')


def return_sum(*args):
    result_sum = sum(args)
    logger.info(f"args uploaded: {result_sum}")
    return result_sum


def return_square_root(number):
    try:
        result_square_root = math.sqrt(number)
        logger.info(f"square_root uploaded: {result_square_root}")
        return result_square_root
    except TypeError:
        logger.exception('Must be real number')


def return_len(string):
    result_len = len(string)
    logger.info(f'Length calculated: {result_len}')
    return result_len


def return_division(x, y):
    try:
        result_division = x / y
        logger.info(f'Results uploaded: {result_division}')
        return result_division
    except ZeroDivisionError:
        logger.exception('Division by zero')


return_sum(2, 6, 8, 7)
return_square_root('hello')
return_len('Hello world')
return_division(1, 0)
