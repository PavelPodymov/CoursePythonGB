"""
Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""
# lst = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
lst = list(map(int, input().strip().split()))

# List comprehension
my_list = [lst[i] for i in range(1, len(lst)) if lst[i - 1] < lst[i]]
print(my_list)

# Generator expression
my_list_1 = (lst[i] for i in range(1, len(lst)) if lst[i - 1] < lst[i])
print([*my_list_1])
