"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета
заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия. Для выполнения расчета для
конкретных значений необходимо запускать скрипт с параметрами.
"""
from sys import argv


def count_earning(time_h, earn_h, prof):
    """Count you earning"""
    return int(time_h) * int(earn_h) + int(prof)


script_name, time_hour, earn_hour, profit = argv
print("Имя скрипта: ", script_name)
print("Выработка: ", time_hour)
print("Ставка: ", earn_hour)
print("Премия: ", profit)
print(f"You earn: {count_earning(time_hour, earn_hour, profit)} rub.")
