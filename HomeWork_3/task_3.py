"""
For checking
Реализовать функцию my_funcs(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_funcs(*args):
    """Take three argument and return sum max of them
    also show sorted tuple and numbers that we will sum"""

    tupl_my = sorted(args)
    print(tupl_my)
    print(*tupl_my[1:])
    print(f"Your sum is: {sum(tupl_my[1:])}")


a, b, c = map(int, input().strip().split())
my_funcs(a, b, c)
