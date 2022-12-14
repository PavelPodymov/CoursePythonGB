"""
Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
"""
from collections import Counter

lst = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# lst = list(map(int, input().strip().split()))


# List comprehension
new_list = [k for k, v in Counter(lst).items() if v == 1]
print(new_list)

new_list_3 = [el for el in lst if lst.count(el) == 1]
print(new_list_3)


# Generator expression
new_list_2 = (k for k, v in Counter(lst).items() if v == 1)
print([*new_list_2])

new_list_4 = (el for el in lst if lst.count(el) == 1)
print([*new_list_4])
