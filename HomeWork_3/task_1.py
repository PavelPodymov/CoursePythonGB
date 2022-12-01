"""
For checking
Реализовать функцию, принимающую два числа (позиционные аргументы) и
выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль.
"""


def division_two_number(numb_1, numb_2):
    """Division two numbers"""
    if numb_2 == 0:
        print("You can't divide because denominator equal '0'")
    else:
        print(numb_1 / numb_2)


STARTS = True
while STARTS:
    nums_1, nums_2 = map(int, input("Your numbers: ").strip().split())
    division_two_number(nums_1, nums_2)
    yes_no = input("N or something: ").lower()
    if yes_no == 'n':
        STARTS = False
