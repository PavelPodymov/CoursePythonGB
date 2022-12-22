"""
HomeWork 4 extra_example_5.py
Даны два файла, в каждом из которых находится запись многочлена.
Задача - сформировать файл, содержащий сумму многочленов.
"""

import random


def write_file(name, some_string):
    """write file"""
    with open(name, 'w', encoding='UTF8') as data_file:
        data_file.write(some_string)


def rnd():
    """Create random number"""
    return random.randint(1, 101)


def create_fun(k):
    """Create coefficient for function"""
    lst = [rnd() for _ in range(k + 1)]
    return lst


def create_str(some_lst):
    """Create function as a string"""
    lst = some_lst[::-1]
    my_str = ''
    lng = len(lst)
    if lng < 1:
        my_str = 'x = 0'
    else:
        for ind, elem in enumerate(lst):
            if ind != lng - 1 and elem != 0 and ind != lng - 2:
                my_str += f'{elem}x^{lng - ind - 1}'
                if lst[ind + 1] != 0 or lst[ind + 2] != 0:
                    my_str += ' + '
            elif ind == lng - 2 and elem != 0:
                my_str += f'{elem}x'
                if lst[ind + 1] != 0 or lst[ind + 2] != 0:
                    my_str += ' + '
            elif ind == lng - 1 and elem != 0:
                my_str += f'{elem} = 0'
            elif ind == lng - 1 and elem == 0:
                my_str += ' = 0'
    return my_str


def sq_mn(k):
    """get power of function"""
    if 'x^' in k:
        index = k.find('^')
        num = int(k[index + 1:])
    elif ('x' in k) and ('^' not in k):
        num = 1
    else:
        num = -1
    return num


def k_mn(k):
    """get coefficient for function"""
    conf = None
    if 'x' in k:
        index = k.find('x')
        conf = int(k[:index])
    return conf


def calc_mn(my_str):
    """get coefficient from function"""
    my_str = my_str[0].replace(' ', '').split('=')
    my_str = my_str[0].split('+')
    lst = []
    lng = len(my_str)
    if sq_mn(my_str[-1]) == -1:
        lst.append(int(my_str[-1]))
        lng -= 1
    power = 1
    index = lng - 1
    while index >= 0:
        if sq_mn(my_str[index]) != -1 and sq_mn(my_str[index]) == power:
            lst.append(k_mn(my_str[index]))
            index -= 1
            power += 1
        else:
            lst.append(0)
            power += 1
    return lst


# k1 = int(input("Input power for first function k = "))
# k2 = int(input("Input power for second function k = "))
k_2 = 3
k_1 = 3
my_cof_1 = create_fun(k_1)
# print(my_cof_1)
my_cof_2 = create_fun(k_2)
# print(my_cof_2)
write_file("file_1.txt", create_str(my_cof_1))
# print(create_str(my_cof_1))
write_file("file_2.txt", create_str(my_cof_2))

with open('file_1.txt', 'r', encoding='UTF8') as data:
    fun_1 = data.readlines()
with open('file_2.txt', 'r', encoding='UTF8') as data:
    fun_2 = data.readlines()
# print(f"First function: {fun_1}")
# print(calc_mn(fun_1))
# print(f"Second function: {fun_2}")
lst_1 = calc_mn(fun_1)
lst_2 = calc_mn(fun_2)
# print(calc_mn(fun_1))
LNG_1 = len(lst_1)
LNG_2 = len(lst_2)
if LNG_1 > LNG_2:
    for i in range(LNG_2, LNG_1):
        lst_2.append(0)
else:
    for i in range(LNG_1, LNG_2):
        lst_1.append(0)

lst_new = [lst_1[i] + lst_2[i] for i in range(len(lst_1))]

write_file("file_res.txt", create_str(lst_new))
with open('file_res.txt', 'r', encoding='UTF8') as data:
    fun_res = data.readlines()
# print(f"Answer: {fun_res}")
