"""
For checking
Задайте список из вещественных чисел. Напишите программу, которая найдёт
разницу между максимальным и минимальным значением дробной части элементов.
Пример:
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
"""


def diff_min_max(some_lst):
    """minus fractional parts max and min"""
    min_prt, max_prt = some_lst[0] % 1, some_lst[0] % 1
    for i in some_lst:
        if i % 1 > max_prt:
            max_prt = i % 1
        elif i % 1 < min_prt:
            min_prt = i % 1
    return max_prt - min_prt


my_lst = list(map(float, input("Input your numb-s: ").strip().split()))
result = diff_min_max(my_lst)
print(f"{result:.2f}")
print(result)
