"""
For checking
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_funcs(*args):
    """Take three argument and return sum max of them
    also show sorted tuple and numbers that we will sum"""
    my_tuple = sorted(args)
    print(my_tuple)
    print(*my_tuple[1:])
    print(f"Your sum is: {sum(my_tuple[1:])}")


a, b, c = map(int, input().strip().split())
my_funcs(a, b, s)
