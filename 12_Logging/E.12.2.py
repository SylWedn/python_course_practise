"""
Perdaryti 1 užduoties programą, kad:
    * Į šaknies funkciją padavus string tipo argumetrą, į log
        failą būtų išsaugoma išimties klaida su norimu tekstu
    * Į dalybos funkciją antrą argumentą padavus 0, į log failą
        būtų išsaugoma išimties klaida su norimu tekstu

Patarimas: panaudoti try/except/else, logging.exception()
"""

import math
import logging

logging.basicConfig(filename="logeris.log",
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

logging.info('<Warning message.>')


def return_sum(*args):
    result_sum = sum(args)
    logging.info(f"args uploaded: {result_sum}")
    return result_sum


def return_square_root(number):
    try:
        result_square_root = math.sqrt(number)
        logging.info(f"square_root uploaded: {result_square_root}")
        return result_square_root
    except TypeError:
        logging.exception('Must be real number')


def return_len(string):
    result_len = len(string)
    logging.info(f'Length calculated: {result_len}')
    return result_len


def return_division(x, y):
    try:
        result_division = x / y
        logging.info(f'Results uploaded: {result_division}')
        return result_division
    except ZeroDivisionError:
        logging.exception('Division by zero')


return_sum(2, 6, 8, 7)
return_square_root('hello')
return_len('Hello world')
return_division(1, 0)