"""
For checking
Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно,
в программе.
"""
my_list = [1, 0.5, 'string', False, 5 + 6j, None]

new_list = {element: type(element) for i, element in enumerate(my_list)}
print(new_list)

for i in my_list:
    print(i, type(i))
