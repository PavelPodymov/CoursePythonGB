8
Filename: D:\GeekBrains\Python\CoursePythonGB\HomeWork_6\code_2.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    10     22.2 MiB     22.2 MiB           1   @profile()
    11                                         def max_number(number):
    12                                             """find maximum number from input number"""
    13     22.2 MiB      0.0 MiB           1       count = 1
    14     22.2 MiB      0.0 MiB           1       lng = len(number)
    15     22.2 MiB      0.0 MiB           2       while count < lng:
    16     22.2 MiB      0.0 MiB           1           max_num = int(number[0])
    17     22.2 MiB      0.0 MiB           9           for i in range(1, lng):
    18     22.2 MiB      0.0 MiB           8               if int(number[i]) > max_num:
    19     22.2 MiB      0.0 MiB           2                   max_num = int(number[i])
    20     22.2 MiB      0.0 MiB           8               count += 1
    21     22.2 MiB      0.0 MiB           1           print(max_num)


8
Filename: D:\GeekBrains\Python\CoursePythonGB\HomeWork_6\code_2.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    24     22.2 MiB     22.2 MiB           1   @profile()
    25                                         def max_number_2(num):
    26                                             """find maximum number from input number"""
    27     22.2 MiB      0.0 MiB           1       count = 0
    28     22.2 MiB      0.0 MiB           1       numb = int(num)
    29     22.2 MiB      0.0 MiB           1       max_numb = int(num) % 10
    30     22.2 MiB      0.0 MiB           9       while count < len(num) - 1:
    31     22.2 MiB      0.0 MiB           8           numb = int(numb / 10)
    32     22.2 MiB      0.0 MiB           8           ans = numb % 10
    33     22.2 MiB      0.0 MiB           8           if ans > max_numb:
    34                                                     max_numb = ans
    35     22.2 MiB      0.0 MiB           8           count += 1
    36     22.2 MiB      0.0 MiB           1       print(max_numb)


8
Filename: D:\GeekBrains\Python\CoursePythonGB\HomeWork_6\code_2.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    39     22.2 MiB     22.2 MiB           1   @profile()
    40                                         def max_number_3(num):
    41                                             """find maximum number from input number 3"""
    42     22.2 MiB      0.0 MiB          21       print(max((num[i] for i in range(len(num)))))


def max_number(number)  0.012774499948136508
def max_number_2(num)   0.019461399991996586
def max_number_3(num)   0.0270066000521183

Process finished with exit code 0