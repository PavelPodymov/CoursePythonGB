"""
Задана натуральная степень k. Сформировать случайным образом список
коэффициентов (значения от 0 до 100) многочлена и записать в
файл многочлен степени k.
Пример:
- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
"""

import random


def write_file(some_string):
    """create file.txt"""
    with open('file.txt', 'w', encoding='UTF8') as data:
        data.write(some_string)


def get_list(some_k):
    """get a list with random numbers"""
    rand_kof_list = [
        f"{random.randint(0, 101)}" \
        f"{'x' if i < some_k else ''}" \
        f"{'^' if some_k - i > 1 else ''}" \
        f"{some_k - i if some_k - i > 1 else ''}"
        for i in range(some_k + 1)]
    return rand_kof_list


def get_string(some_lst):
    """Create string"""
    my_string = ''
    lng = len(some_lst)
    if not some_lst:
        my_string = "0 = 0"
    elif len(some_lst) == 1 and some_lst[0].isnumeric():
        my_string = f"{some_lst[0]} != 0"
    else:
        for i in range(lng + 1):
            if i == lng:
                my_string += ' = 0'
            elif i == lng - 1:
                my_string += f' {str(some_lst[lng - i - 1])} '
            else:
                my_string += f' {str(some_lst[lng - i - 1])} + '
    return my_string


k = int(input("Your power K = "))
new_lst = [i for i in get_list(k)[::-1] if i[0] != '0']
write_file(get_string(new_lst))
