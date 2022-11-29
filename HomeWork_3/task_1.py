"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и
выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль.
"""


def division_two_numbers(num_1, num_2):
    """Division two numbers"""
    if num_2 == 0:
        print("You can't divide because denominator equal '0'")
    else:
        print(num_1 / num_2)


START = True
while START:
    nums_1, nums_2 = map(int, input("Your numbers: ").strip().split())
    division_two_numbers(nums_1, nums_2)
    yes_no = input("N or something: ").lower()
    if yes_no == 'n':
        START = False
