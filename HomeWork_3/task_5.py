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
RESULTS = 0
while STARTS:
    you_numb = list(input("List of number: ").strip().split())
    CNT = 0
    length_lst = len(you_numb)
    while CNT < length_lst:

        if you_numb[CNT].lower() == 'n':
            CNT = length_lst
            STARTS = False
        else:
            try:
                RESULTS += int(you_numb[CNT])
                CNT += 1
            except ValueError:
                CNT += 1

    print(RESULTS)
    if STARTS is not True:
        STARTS = False
    elif input("Write N or miss: ").lower() == 'n':
        STARTS = False
