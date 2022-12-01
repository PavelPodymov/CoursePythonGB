"""
For checking
Программа принимает действительное положительное число x и целое отрицательное
число y. Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_funcs(x, y).
При решении задания необходимо обойтись без встроенной функции возведения
числа в степень.
Подсказка: попробуйте решить задачу двумя способами.
Первый — возведение в степень с помощью оператора *.
Второй — более сложная реализация без оператора *, предусматривающая
использование цикла.
"""

# First decision


def my_func_11(x_ar, y_ar):
    """return power"""
    return x_ar ** y_ar


# Second decision



def my_func_21(x_ar, y_ar):
    """return power"""

    def multi(x_a, y_a):
        multipli = 1
        for _ in range(abs(y_a)):
            multipli *= x_a
        return multipli

    if y_ar < 0:
        result = 1 / multi(x_ar, y_ar)
    else:
        result = multi(x_ar, y_ar)
    return result


x_arg = int(input("Your numb (x > 0 and type - int) X: "))
y_arg = int(input("Your numb (y < 0 and type - int) Y: "))

print(my_func_11(x_arg, y_arg))
print(my_func_21(x_arg, y_arg))

