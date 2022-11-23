"""
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

"""
# CONSTANT
NUMBER = ''
ANSWER = 0

user_number = input("Please input your number: ")

for i in range(3):
    NUMBER += user_number
    ANSWER += int(NUMBER)
print(ANSWER)
