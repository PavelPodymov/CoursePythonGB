"""
Реализуйте алгоритм перемешивания списка.
"""
from random import randint


def get_list(num):
    """get random list"""
    return list(range(1, num + 1))


def get_unsorted_list(some_list):
    """unsorted list"""
    len_list = len(some_list)
    for i in range(len_list):
        num = randint(0, len_list - 1)
        some_list[i], some_list[num] = some_list[num], some_list[i]
    return some_list


number = int(input("Your number: "))
my_list = get_list(number)
print(my_list)
print(get_unsorted_list(my_list))
