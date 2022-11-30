"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(*args):
    """Take three argument and return sum max of them
    also show sorted tuple and numbers that we will sum"""
    tuple_my = sorted(args)
    print(tuple_my)
    print(*tuple_my[1:])
    print(f"Your sum is: {sum(tuple_my[1:])}")


a, b, s = map(int, input().strip().split())
my_func(a, b, s)
