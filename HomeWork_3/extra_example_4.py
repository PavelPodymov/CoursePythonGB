"""
For checking
Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Пример:
- 45 -> 101101
- 3 -> 11
- 2 -> 10
"""


def dec_binar(some_n, result=''):
    """convert number to binary number"""
    if some_n != 0:
        result += dec_binar(some_n // 2, result) + str(some_n % 2)
    return result


print(dec_binar(5))
print(dec_binar(43))
print(dec_binar(2))
print(dec_binar(2))
