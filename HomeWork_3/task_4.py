"""
For checking
Программа принимает действительное положительное число x и целое отрицательное
число y. Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения
числа в степень.
Подсказка: попробуйте решить задачу двумя способами.
Первый — возведение в степень с помощью оператора *.
Второй — более сложная реализация без оператора *, предусматривающая
использование цикла.
"""


# First decision


def my_func_1(x_argym, y_argym):
    """return power"""
    return x_argym ** y_argym


# Second decision


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


x_arg = int(input("Your numb (x > 0 and type - int) X: "))
y_arg = int(input("Your numb (y < 0 and type - int) Y: "))
print(my_func_1(x_arg, y_arg))
print(my_func_21(x_arg, y_arg))
