"""
1. Создать текстовый файл (не программно), : task_3_file.txt
2. Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
3. Определить, кто из сотрудников имеет оклад менее 20 тыс.,
4. Вывести фамилии этих сотрудников.
5. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""
from functools import reduce

with open('task_3_file.txt', encoding='utf-8') as data:
    my_list = data.readlines()


def sum_numbers(first, next_el):
    """sum numbers"""
    return first + next_el


def less_20000(some_list):
    """find person with income less than 20 000"""
    for element in some_list:
        n_el = element.split()
        try:
            if float(n_el[1]) < 20000:
                print(f"Name: {n_el[0]};\tEarning = {n_el[1]}")
        except IndexError:
            continue


def average_earning(list_el):
    """return average earning"""
    list_earn = []
    for elem in list_el:
        try:
            list_earn.append(float(elem.split()[1]))
        except IndexError:
            continue
    my_sum = reduce(sum_numbers, list_earn)
    return my_sum / len(list_earn)


print("1. Person who have earn less than 20 000 rub.: \n")
less_20000(my_list)
print(f"\n2. Average earning all person is: {average_earning(my_list):.2f}")
