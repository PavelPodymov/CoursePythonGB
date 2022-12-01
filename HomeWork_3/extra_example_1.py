"""
For checking
Задайте список из нескольких чисел. Напишите программу,
которая найдёт сумму элементов списка, стоящих на нечётной позиции.
Пример:

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
"""

you_list = list(map(int, input("Input your numbers: ").strip().split()))
SUM_ODD = 0
for i, el in enumerate(you_list):
    if i % 2 != 0:
        SUM_ODD += el
print(SUM_ODD)
