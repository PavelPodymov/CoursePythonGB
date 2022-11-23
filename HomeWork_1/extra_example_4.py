"""
Напишите программу, которая по заданному номеру четверти, показывает диапазон
возможных координат точек в этой четверти (x и y).

"""


def find_coordinate_from_quarter(some_quarter):
    """find quarter from coordinates when x != 0 and y != 0"""
    if some_quarter == 1:
        print("coordinate: (+∞; +∞)")
    elif some_quarter == 2:
        print("coordinate: (-∞; +∞)")
    elif some_quarter == 3:
        print("coordinate: (-∞; -∞)")
    else:
        print("coordinate: (+∞; -∞)")


try:
    quarter = int(input("Please input quarter = "))
    if 0 < quarter < 5:
        find_coordinate_from_quarter(quarter)
    else:
        print("You write wrong quarter")
except ValueError:
    print("You write wrong number")
