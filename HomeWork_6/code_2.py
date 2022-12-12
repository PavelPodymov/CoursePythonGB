"""
1) Из ваших заданий в уроках 1-5 найти 2-3 скрипта, сделать замеры времени, оптимизировать,
вновь выполнить замеры и подготовить аналитику, что вы сделали и чего удалось добиться.
2) Из ваших заданий в уроках 1-5 найти 2-3 скрипта, сделать замеры памяти, оптимизировать,
вновь выполнить замеры и подготовить аналитику, что вы сделали и чего удалось добиться.
"""
from memory_profiler import profile


@profile()
def max_number(number):
    """find maximum number from input number"""
    count = 1
    lng = len(number)
    while count < lng:
        max_num = int(number[0])
        for i in range(1, lng):
            if int(number[i]) > max_num:
                max_num = int(number[i])
            count += 1
        print(max_num)


@profile()
def max_number_2(num):
    """find maximum number from input number"""
    count = 0
    numb = int(num)
    max_numb = int(num) % 10
    while count < len(num) - 1:
        numb = int(numb / 10)
        ans = numb % 10
        if ans > max_numb:
            max_numb = ans
        count += 1
    print(max_numb)


@profile()
def max_number_3(num):
    """find maximum number from input number 3"""
    print(max((num[i] for i in range(len(num)))))


max_number('111141118')
max_number_2('111141118')
max_number_3('111141118')

# по весу не увидел существенных отличий кроме как в параметре
# Occurrences - в def max_number_3 (вхождений) меньше всего
# отработку функций по памяти и скорости смотри файл code_2.md
