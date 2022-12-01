"""
For checking
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел. Пользователь может
продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы
завершается. Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и
после этого завершить программу.
"""

STARTS = True
RESULTs = 0
while STARTS:
    you_numbs = list(input("List of number: ").strip().split())
    COUNT = 0
    len_list = len(you_numbs)
    while COUNT < len_list:

        if you_numbs[COUNT].lower() == 'n':
            COUNT = len_list
            STARTS = False
        else:
            try:
                RESULTs += int(you_numbs[COUNT])
                COUNT += 1
            except ValueError:
                COUNT += 1

    print(RESULTs)
    if STARTS is not True:
        STARTS = False
    elif input("Continue write N or miss: ").lower() == 'n':
        STARTS = False
