"""
Задайте список из n чисел последовательности $(1+\frac 1 n)^n$
и выведите на экран их сумму.
Пример:
!!! Ошибка в примере: функция не соответствует ответу
- Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
"""

n = int(input("Your number: "))
my_list = [round((1 + 1 / i) ** i, 3) for i in range(1, n + 1)]
my_dict = {i: round((1 + 1 / i) ** i, 3) for i in range(1, n + 1)}

result = sum(my_list)
result2 = sum(my_dict.values())
print(my_list)
print(my_dict)
print(result)
print(result2)
