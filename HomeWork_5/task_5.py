"""
1. Создать (программно) текстовый файл,
2. записать в него программно набор чисел, разделенных пробелами.
3. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

with open('task_5_file.txt', 'w', encoding='utf8') as file:
    file.write(input('Введите числа через пробел: '))
with open('task_5_file.txt', encoding='utf8') as data:
    d = data.read().split()


def count_sum_list(some_list):
    """Count sum in some list"""
    my_list = []
    for i in some_list:
        try:
            my_list.append(int(i))
        except ValueError:
            pass
    print(sum(my_list))


count_sum_list(d)
