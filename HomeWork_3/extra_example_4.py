"""
For checking
Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Пример:
- 45 -> 101101
- 3 -> 11
- 2 -> 10
"""


def dec_binary(some_num, res=''):
    """convert number to binary number"""
    if some_num != 0:
        res += dec_binary(some_num // 2, res) + str(some_num % 2)
    return res


print(dec_binary(5))
print(dec_binary(43))
print(dec_binary(2))
print(dec_binary(2))
