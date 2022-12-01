"""
For checking
Реализовать функцию, принимающую два числа (позиционные аргументы) и
выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль.
"""


def divi_two_numb(numb_1, numb_2):
    """Division two numbers"""
    if numb_2 == 0:
        print("You can't divide because denominator equal '0'")
    else:
        print(numb_1 / numb_2)


STAR = True
while STAR:
    numm_1, numm_2 = map(int, input("Your numbers: ").strip().split())
    divi_two_numb(numm_1, numm_2)
    no_continue = input("N or something: ").lower()
    if no_continue == 'n':
        STAR = False
