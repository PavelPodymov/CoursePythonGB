"""
For checking
Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Пример:
- 45 -> 101101
- 3 -> 11
- 2 -> 10
"""


def dec_bin(some_n, result=''):
    """convert number to binary number"""
    if some_n != 0:
        result += dec_bin(some_n // 2, result) + str(some_n % 2)
    return result


print(dec_bin(45))
print(dec_bin(3))
print(dec_bin(2))
print(dec_bin(3))
