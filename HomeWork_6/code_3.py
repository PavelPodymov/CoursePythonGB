"""
1) Из ваших заданий в уроках 1-5 найти 2-3 скрипта, сделать замеры времени, оптимизировать,
вновь выполнить замеры и подготовить аналитику, что вы сделали и чего удалось добиться.
2) Из ваших заданий в уроках 1-5 найти 2-3 скрипта, сделать замеры памяти, оптимизировать,
вновь выполнить замеры и подготовить аналитику, что вы сделали и чего удалось добиться.
"""
from memory_profiler import profile



@profile()
def my_func_1(x_argym, y_argym):
    """return power"""
    return x_argym ** y_argym


# Second decision

@profile()
def my_func_21(x_args, y_args):
    """return power"""

    def multi(x_ar, y_ar):
        multiply = 1
        for _ in range(abs(y_ar)):
            multiply *= x_ar
        return multiply

    if y_args < 0:
        results = 1 / multi(x_args, y_args)
    else:
        results = multi(x_args, y_args)
    return results


print(my_func_1(2, 32))
print(my_func_21(2, 32))

# отработку функций по памяти и скорости смотри файл code_3.md
