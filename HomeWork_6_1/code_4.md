1! 1
2! 2
3! 6
4! 24
5! 120
6! 720
7! 5040
8! 40320
Filename: D:\GeekBrains\Python\CoursePythonGB\HomeWork_6\code_4.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    12     22.3 MiB     22.3 MiB           1   @profile()
    13                                         def fact_list(some_n=8):
    14                                             """generator"""
    15     22.3 MiB      0.0 MiB          76       my_list = [reduce(lambda x, y: x * y, range(1, j + 1))
    16     22.3 MiB      0.0 MiB           9                  for j in range(1, some_n + 1)]
    17     22.3 MiB      0.0 MiB           9       for i, elem in enumerate(my_list, start=1):
    18     22.3 MiB      0.0 MiB           8           print(f"{i}! {elem}")


1! 1
2! 2
3! 6
4! 24
5! 120
6! 720
7! 5040
8! 40320
Filename: D:\GeekBrains\Python\CoursePythonGB\HomeWork_6\code_4.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    21     22.3 MiB     22.3 MiB           1   @profile()
    22                                         def fact_diction(some=8):
    23                                             """generator"""
    24     22.3 MiB      0.0 MiB          76       my_dict = {f"{j}!": reduce(lambda x, y: x * y, range(1, j + 1))
    25     22.3 MiB      0.0 MiB           9                  for j in range(1, some + 1)}
    26     22.3 MiB      0.0 MiB           9       for k, val in my_dict.items():
    27     22.3 MiB      0.0 MiB           8           print(k, val)


1! 1
2! 2
3! 6
4! 24
5! 120
6! 720
7! 5040
8! 40320
Filename: D:\GeekBrains\Python\CoursePythonGB\HomeWork_6\code_4.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    30     22.3 MiB     22.3 MiB           1   @profile()
    31                                         def fact_math(nn=8):
    32                                             """Factorial"""
    33     22.3 MiB      0.0 MiB          11       dict_some = {f"{i}!": math.factorial(i) for i in range(1, nn + 1)}
    34     22.3 MiB      0.0 MiB           9       for k, val in dict_some.items():
    35     22.3 MiB      0.0 MiB           8           print(k, val)


def fact_list(some_n=8)     0.012665199930779636
def fact_diction(some=8)    0.01959730009548366
def fact_math(nn=8)         0.023287300020456314

Process finished with exit code 0