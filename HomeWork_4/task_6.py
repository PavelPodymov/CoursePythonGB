"""
Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении
числа 10 завершаем цикл. Во втором также необходимо предусмотреть условие,
при котором повторение элементов списка будет прекращено.
"""
from itertools import count, cycle
from random import randint

start, end, step = map(int, input("you number start, end and step: ").split())
for el in count(start, step=step):
    if el < end:
        print(el)
    else:
        break

CNT = 0
list_my = [randint(start, end) for i in range(1, 11)]
print(list_my)
for el in cycle(list_my):
    if CNT < len(list_my):
        print(el)
    else:
        break
    CNT += 1
COUNTER = 0
STRING = "itertools"
for el in cycle(STRING):
    if COUNTER < len(STRING):
        print(el)
    else:
        break
    COUNTER += 1
