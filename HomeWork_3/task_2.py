"""
For checking
Реализовать функцию, принимающую несколько параметров, описывающих
данные пользователя: имя, фамилия, год рождения, город проживания, email,
телефон. Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def personal_description(**kwargs):
    """Function take information from person"""
    return kwargs


print(personal_description(
    name='Pavel',
    secname='Podymov',
    year=1982,
    city='Lubertsy',
    email='erer@gmail.com',
    phone=123456789
))


