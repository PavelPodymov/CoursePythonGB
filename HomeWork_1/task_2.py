"""
Пользователь вводит время в секундах. Переведите время в часы,
минуты и секунды и выведите в формате чч:мм:сс. Используйте
форматирование строк.
"""

user_time = int(input("Please input your information: "))
days = int(user_time // 60 // 60 // 24)
hour = int(user_time // 60 // 60)
if hour > 24:
    hour = int((user_time - days * 60 * 60 * 24) // 60 // 60)

seconds = int(user_time % 60)

if days > 0:
    minute = (user_time - seconds - (hour * 60 * 60) - (
                days * 60 * 60 * 24)) // 60
    print(f"days:{days} [{hour:02}:{minute:02}:{seconds:02}]")
else:
    minute = (user_time - seconds - hour * 60 * 60) // 60
    print(f"{hour:02}:{minute:02}:{seconds:02}")
