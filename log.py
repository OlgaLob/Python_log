from complex import a
from complex import b
from complex import rez
from input import prc
from input import d
from input import result


import logging


logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="a",
                    format="%(asctime)s %(levelname)s %(message)s")


def test_division(a,b):
    logging.info(f"The values of 'a' and 'b' are {a} and {b}.")
    try:
        a/b
        logging.info(f"'a / b' successful with result: {rez}.")
    except ZeroDivisionError as err:
        logging.error("ZeroDivisionError",exc_info=True)


def test_sum(a,b):
    logging.info(f"The values of 'a' and 'b' are {a} and {b}.")
    logging.info(f"'a + b' successful with result: {rez}.")

def test_diff(a,b):
    logging.info(f"The values of 'a' and 'b' are {a} and {b}.")
    logging.info(f"'a - b' successful with result: {rez}.")

def test_mult(a,b):
    logging.info(f"The values of 'a' and 'b' are {a} and {b}.")
    logging.info(f"'a * b' successful with result: {rez}.")

def test_sqwt(a):
    logging.info(f"The value of 'a' is {a}.")
    logging.info(f"square root a successful with result: {rez}.")

def test_perсent(d, prс):
    logging.info(f"The value of 'a' is {d}.")
    logging.info(f"{prc} % of {d} a successful with result: {result}.")
    
#test_division(a,b)
#test_sum(a,b)
#test_diff(a,b)
#test_mult(a,b)
#test_sqwt(a)
test_perсent(d, prc)
