"""
Напишите программу, которая принимает на вход координаты точки (X и Y).
Причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
"""


def find_quoter(x_cord, y_cord):
    """find quoter from coordinates when x != 0 and y != 0"""
    if x_cord > 0:
        if y_cord > 0:
            print(f"x = {x_cord}; y = {y_cord} -> 1st - quoter")
        else:
            print(f"x = {x_cord}; y = {y_cord} -> 4th - quoter")
    else:
        if y_cord > 0:
            print(f"x = {x_cord}; y = {y_cord} -> 2nd - quoter")
        else:
            print(f"x = {x_cord}; y = {y_cord} -> 3rd - quoter")


def check_position_coordinate(x_cord, y_cord):
    """check coordinate may be dot lay on the axis"""
    if x_cord == 0:
        if y_cord == 0:
            print("Your coordinate (0; 0) - is center")
        else:
            print(f"Your coordinate (0; {y_cord}) - dot on the axis Y")
    else:
        if y_cord == 0:
            print(f"Your coordinate ({x_cord}; 0) - dot on the axis X")
        else:
            find_quoter(x_cord, y_cord)


try:
    x = int(input("Please input x = "))
    y = int(input("Please input y = "))
    check_position_coordinate(x, y)
except ValueError:
    print("You write wrong coordinate")
