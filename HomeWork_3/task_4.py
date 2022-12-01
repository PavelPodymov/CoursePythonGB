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


def my_func_1(x_ar, y_ar):
    """return power"""
    return x_ar ** y_ar


# Second decision



def my_func_2(x_ar, y_ar):
    """return power"""

    def mult(x_a, y_a):
        multiply = 1
        for _ in range(abs(y_a)):
            multiply *= x_a
        return multiply

    if y_ar < 0:
        result = 1 / mult(x_ar, y_ar)
    else:
        result = mult(x_ar, y_ar)
    return result


x_arg = int(input("Your number (x > 0 and type - int) X: "))
y_arg = int(input("Your number (y < 0 and type - int) Y: "))

print(my_func_1(x_arg, y_arg))
print(my_func_2(x_arg, y_arg))
