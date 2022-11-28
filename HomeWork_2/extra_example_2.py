"""
For checking
Напишите программу, которая принимает на вход число N и выдает
набор произведений чисел от 1 до N.
Пример:
- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
"""
NUMBER = int(input("Your number: "))
my_list = []
for i in range(1, NUMBER + 1):
    if i == 1:
        my_list.append(i)
    else:
        my_list.append(i * my_list[i - 2])

print(my_list)
