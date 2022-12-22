"""
HomeWork 4 task_7.py

Реализовать генератор с помощью функции с ключевым словом yield,
создающим очередное значение. При вызове функции должен создаваться
объект-генератор. Функция должна вызываться следующим образом:
for el in fact(n). Функция отвечает за получение факториала числа,
а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например,
факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""
from functools import reduce


def fact(some_n):
    """generator"""
    return reduce(lambda x, y: x * y, range(1, some_n + 1))


def fact_list(some_n):
    """generator"""
    my_list = [reduce(lambda x, y: x * y, range(1, j + 1))
               for j in range(1, some_n + 1)]
    return my_list


def fact_diction(some):
    """generator"""
    my_dict = {f"{j}!": reduce(lambda x, y: x * y, range(1, j + 1))
               for j in range(1, some + 1)}
    for k, val in my_dict.items():
        yield k, val


# you_number = int(input("Your number: "))

# for el in fact(you_number):
#     print(f"{you_number}! = {el}")
#
# print(*fact_diction(you_number))
# # or
# for el in fact_diction(you_number):
#     print(f"{el}")

# print(fact_list(6))
# or
# for el in fact_list(you_number):
#     print(el)
