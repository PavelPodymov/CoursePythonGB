"""Class ZeroDivisionException"""


class ZeroDivisionException(Exception):
    """divide by zero"""

    def __init__(self, text):
        self.text = text


def my_function():
    """my function"""
    n_data = 1
    d_data = 0
    if d_data == 0:
        raise ZeroDivisionException("Your denominator = 0, you can't do division")
    return n_data / d_data


def my_function_2():
    """My function"""
    a = 1 / 0
    return a
