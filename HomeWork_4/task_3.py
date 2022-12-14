"""
Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генератор.
"""

# List comprehension
new_list_1 = [el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]
print(new_list_1)

print([el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0])

# Generator expression
new_list = (el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0)
for i in new_list:
    print(i)

print(*(el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0))
