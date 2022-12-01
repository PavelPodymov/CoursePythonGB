"""
For checking
Задайте число. Составьте список чисел Фибоначчи,
в том числе для отрицательных индексов.
Пример:
- для k = 8 список будет выглядеть так:
[-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]
"""


def fib(sm_num):
    """Fibonacci"""
    if sm_num in {0, 1}:
        return sm_num
    return fib(sm_num - 1) + fib(sm_num - 2)


def fib_neg(some_num):
    """negative index Fibonacci"""
    if some_num == -1:
        return 1
    if some_num == -2:
        return -1
    return fib_neg(some_num + 2) - fib_neg(some_num + 1)


your_number = int(input("Your number: "))
list_my_1 = [fib(n) for n in range(your_number + 1)]
list_my_2 = [fib_neg(n) for n in range(-your_number, 0)]

print(list_my_1)
print(list_my_2)
print(list_my_2 + list_my_1)

