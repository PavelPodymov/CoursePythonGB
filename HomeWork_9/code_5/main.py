"""
HomeWork 3 extra_example_5.py
Задайте число. Составьте список чисел Фибоначчи,
в том числе для отрицательных индексов.
Пример:
- для k = 8 список будет выглядеть так:
[-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]
"""


def fibo(som_num):
    """Fibonacci"""
    if som_num in {0, 1}:
        return som_num
    return fibo(som_num - 1) + fibo(som_num - 2)


def fibo_neg(some_numb):
    """negative index Fibonacci"""
    if some_numb == -1:
        return 1
    if some_numb == -2:
        return -1
    return fibo_neg(some_numb + 2) - fibo_neg(some_numb + 1)

# your_number = int(input("Your number: "))
# lst_my_1 = [fibo(n) for n in range(your_number + 1)]
# lst_my_2 = [fibo_neg(n) for n in range(-your_number, 0)]

# print(lst_my_1)
# print(lst_my_2)
# print(lst_my_2 + lst_my_1)
