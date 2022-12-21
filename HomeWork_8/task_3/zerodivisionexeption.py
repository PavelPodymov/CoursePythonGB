"""Class ZeroDivisionException"""


class ZeroDivisionException(Exception):
    """divide by zero"""

    def __init__(self, text):
        self.text = text
