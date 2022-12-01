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
START = True
RESULT = 0
while START:
    you_numbers = list(input("List of number: ").strip().split())
    COUNT = 0
    len_num_list = len(you_numbers)
    while COUNT < len_num_list:

        if you_numbers[COUNT].lower() == 'n':
            COUNT = len_num_list
            START = False
        else:
            try:
                RESULT += int(you_numbers[COUNT])
                COUNT += 1
            except ValueError:
                COUNT += 1

    print(RESULT)
    if START is not True:
        START = False
    elif input("Continue write N or miss: ").lower() == 'n':
        START = False

