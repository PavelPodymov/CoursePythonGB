"""
For checking
Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Пример:
- 45 -> 101101
- 3 -> 11
- 2 -> 10
"""


def dec_binary(some_num, results=''):
    """convert number to binary number"""
    if some_num != 0:
        results += dec_binary(some_num // 2, results) + str(some_num % 2)
    return results


print(dec_binary(5))
print(dec_binary(43))
print(dec_binary(2))
print(dec_binary(2))
