"""
Задайте натуральное число N. Напишите программу,
которая составит список простых множителей числа N.
"""


def get_list(some_num):
    """get list"""
    i = 2
    lst = []
    while i <= some_num:
        if some_num % i == 0:
            lst.append(i)
            some_num /= i
            i = 2
        else:
            i += 1
    return lst


num = int(input("Your number: "))
print(f"Your number is: {num}; list of simple multiply: {get_list(num)}")
