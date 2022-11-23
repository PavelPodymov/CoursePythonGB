"""
Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""


def max_number(number):
    """find maximum number from input number"""
    count = 1
    while count < len(number):
        max_num = int(number[0])
        for i in range(1, len(number)):
            if int(number[i]) > max_num:
                max_num = int(number[i])
            count += 1
        print(max_num)


user_number = input("Please input your number: ")
max_number(user_number)


def max_number_2(num):
    """find maximum number from input number"""
    count = 0
    numb = int(num)
    max_numb = int(num) % 10
    while count < len(num)-1:
        numb = int(numb / 10)
        ans = numb % 10
        if ans > max_numb:
            max_numb = ans
        count += 1
    print(max_numb)


# user_number2 = input("Please input your number: ")
# max_number_2(user_number2)
