"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""

seasons = {'winter': [12, 1, 2], 'spring': [3, 4, 5], 'summer': [6, 7, 8],
           'autumn': [9, 10, 11]}

month = int(input("You month is: "))
for key, value in seasons.items():
    if month in value:
        print(key)
