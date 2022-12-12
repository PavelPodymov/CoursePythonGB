Filename: D:\GeekBrains\Python\CoursePythonGB\HomeWork_6\code_3.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    12     22.1 MiB     22.1 MiB           1   @profile()
    13                                         def my_func_1(x_argym, y_argym):
    14                                             """return power"""
    15     22.1 MiB      0.0 MiB           1       return x_argym ** y_argym


4294967296
Filename: D:\GeekBrains\Python\CoursePythonGB\HomeWork_6\code_3.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    20     22.1 MiB     22.1 MiB           1   @profile()
    21                                         def my_func_21(x_args, y_args):
    22                                             """return power"""
    23                                         
    24     22.1 MiB      0.0 MiB           2       def multi(x_ar, y_ar):
    25     22.1 MiB      0.0 MiB           1           multiply = 1
    26     22.1 MiB      0.0 MiB          33           for _ in range(abs(y_ar)):
    27     22.1 MiB      0.0 MiB          32               multiply *= x_ar
    28     22.1 MiB      0.0 MiB           1           return multiply
    29                                         
    30     22.1 MiB      0.0 MiB           1       if y_args < 0:
    31                                                 results = 1 / multi(x_args, y_args)
    32                                             else:
    33     22.1 MiB      0.0 MiB           1           results = multi(x_args, y_args)
    34     22.1 MiB      0.0 MiB           1       return results


4294967296
def my_func_1(x_argym, y_argym) = 0.02910609997343272
def my_func_21(x_args, y_args)  = 0.043047400075010955