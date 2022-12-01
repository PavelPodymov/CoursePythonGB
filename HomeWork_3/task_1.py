"""
For checking
Реализовать функцию, принимающую два числа (позиционные аргументы) и
выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль.
"""


def division_two_number(number_1, number_2):
    """Division two numbers"""
    if number_2 == 0:
        print("You can't divide because denominator equal '0'")
    else:
        print(number_1 / number_2)


START = True
while START:
    num_1, nums_2 = map(int, input("Your numbers: ").strip().split())
    division_two_number(num_1, nums_2)
    yes_no = input("N or something: ").lower()
    if yes_no == 'n':
        START = False
