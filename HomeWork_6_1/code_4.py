"""
1) Из ваших заданий в уроках 1-5 найти 2-3 скрипта, сделать замеры времени, оптимизировать,
вновь выполнить замеры и подготовить аналитику, что вы сделали и чего удалось добиться.
2) Из ваших заданий в уроках 1-5 найти 2-3 скрипта, сделать замеры памяти, оптимизировать,
вновь выполнить замеры и подготовить аналитику, что вы сделали и чего удалось добиться.
"""
from functools import reduce
import math
from memory_profiler import profile


@profile()
def fact_list(some_n=8):
    """generator"""
    my_list = [reduce(lambda x, y: x * y, range(1, j + 1))
               for j in range(1, some_n + 1)]
    for i, elem in enumerate(my_list, start=1):
        print(f"{i}! {elem}")


@profile()
def fact_diction(some=8):
    """generator"""
    my_dict = {f"{j}!": reduce(lambda x, y: x * y, range(1, j + 1))
               for j in range(1, some + 1)}
    for k, val in my_dict.items():
        print(k, val)


@profile()
def fact_math(my_num=8):
    """Factorial"""
    dict_some = {f"{i}!": math.factorial(i) for i in range(1, my_num + 1)}
    for k, val in dict_some.items():
        print(k, val)


fact_list()
fact_diction()
fact_math()

# отработку функций по памяти и скорости смотри файл code_4.md
