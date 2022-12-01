"""
For checking
Реализовать функцию, принимающую несколько параметров, описывающих
данные пользователя: имя, фамилия, год рождения, город проживания, email,
телефон. Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def personal_descript(**kwargs):
    """Function take information from person"""

    return kwargs


print(personal_descript(
    names='Pavel',
    secname='Podymov',
    years=1982,
    cities='Lubertsy',
    email='erer@gmail.com',
    phone=123456789
))
