"""Class ZeroDivisionException"""
from zerodivisionexeption import ZeroDivisionException

try:
    n_data = int(input("Numerator     = "))
    d_data = int(input("Denominator   = "))
    if d_data == 0:
        raise ZeroDivisionException("Your denominator = 0, you can't do division")
except ValueError:
    print("You input not a number!")
except ZeroDivisionException as err:
    print(err)
else:
    print(f"Your answer = {n_data / d_data:.1f}")
