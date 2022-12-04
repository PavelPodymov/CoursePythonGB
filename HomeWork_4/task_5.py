"""
Реализовать формирование списка, используя функцию range() и возможности
генератора. В список должны войти четные числа от 100 до 1000
(включая границы). Необходимо получить результат вычисления произведения
всех элементов списка.
Подсказка: использовать функцию reduce().
"""
from functools import reduce


def multiply(some_list):
    """multiply numbers"""
    result = 1
    for i in some_list:
        result *= i
    return result


def multiply_2(first, next_el):
    """multiply numbers"""
    return first * next_el


# List comprehension
new_list_1 = [el for el in range(100, 1001) if el % 2 == 0]
print(new_list_1)
ans_w = reduce(lambda x, y: x * y, new_list_1)
print(ans_w)

# Generator expression
new_list_2 = (el for el in range(100, 1001) if el % 2 == 0)
print([*new_list_2])
new_list_2 = (el for el in range(100, 1001) if el % 2 == 0)
ans = multiply(new_list_2)
print(ans)

new_list_3 = (el for el in range(1, 7) if el % 2 == 0)

# use function reduce()

ans_1 = reduce(multiply_2, new_list_3)
print(ans_1)
# or
# ans = reduce(lambda x, y: x * y, new_list_3)
# print(ans)

answer = reduce(lambda x, y: x * y, range(2, 5, 2))
print(answer)
