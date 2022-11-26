"""
For checking
Напишите программу, которая принимает на вход вещественное число
и показывает сумму его цифр.
Пример:
- 6782 -> 23
- 0,56 -> 11
"""


def sum_numbers_in_number(some_number):
    """ sum numbers from number"""
    result = 0
    while some_number > 1:
        result += int(some_number) % 10
        some_number /= 10
    print(result)


try:
    NUMBER = abs(float(input("Please input the number: ")))
    if NUMBER < 1:
        NUMBER = int(str(NUMBER)[2:])
        sum_numbers_in_number(NUMBER)
    else:
        sum_numbers_in_number(NUMBER)
except ValueError:
    print("You wright something wrong!")
