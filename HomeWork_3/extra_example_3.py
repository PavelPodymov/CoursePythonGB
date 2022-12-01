"""
For checking
Задайте список из вещественных чисел. Напишите программу, которая найдёт
разницу между максимальным и минимальным значением дробной части элементов.

Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
"""

def difference_min_max(some_list):
    """minus fractional parts max and min"""
    min_prt, max_prt = some_list[0] % 1, some_list[0] % 1
    for i in some_list:
        if i % 1 > max_prt:
            max_prt = i % 1
        elif i % 1 < min_prt:
            min_prt = i % 1

    return max_prt - min_prt


my_lst = list(map(float, input("Input your numbers: ").strip().split()))
result = difference_min_max(my_lst)
print(f"{result:.2f}")
print(result)
