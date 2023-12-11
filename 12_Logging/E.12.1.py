"""
Sukurti funkcijas, kurios:
    * Gražintų visų paduotų skaičių sumą (su *args argumentu)
    * Gražintų paduoto skaičiaus šaknį (panaudoti math.sqrt())
    * Gražintų paduoto sakinio simbolių kiekį (su len())
    * Gražintų rezultatą, skaičių x padalinus iš y
Nustatyti standartinį logerį (logging) taip, kad jis:
    * Saugotų pranešimus į norimą failą
    * Saugotų INFO lygio žinutes
    * Pranešimai turi būti tokiu formatu: data/laikas, lygis, žinutė

Kiekviena funkcija turi sukurti INFO lygio log pranešimą apie tai, ką atliko
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
    result_square_root = math.sqrt(number)
    logging.info(f"square_root uploaded: {result_square_root}")
    return result_square_root


def return_len(string):
    result_len = len(string)
    logging.info(f'Length calculated: {result_len}')
    return result_len


def return_division(x, y):
    result_division = x / y
    logging.info(f'Results uploaded: {result_division}')
    return result_division


return_sum(2, 6, 8, 7)
return_square_root(8)
return_len('Hello world')
return_division(8, 2)