"""
Задание 3.
Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" и обработав исключение,
придумайте как это сделать.
"""

list_of_w = ['attribute', 'класс', 'функция', 'type']

for i in list_of_w:
    try:
        print(i, type(i), i.encode('ascii'), ' - successfully, word encoding to bytes')
    except UnicodeEncodeError:
        print(i, type(i), ' - failed, can\'t encoding to bytes')
print()
for i in list_of_w:
    try:
        print(i, type(i), bytes(i, 'ascii'), ' - successfully, word encoding to bytes')
    except UnicodeEncodeError:
        print(i, type(i), ' - failed, can\'t encoding to bytes')
