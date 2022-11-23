"""
Запросите у пользователя значения выручки и издержек фирмы. Определите,
с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки
(соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите
прибыль фирмы в расчете на одного сотрудника.
"""

proceeds = int(input("Please input your proceeds, rub: "))
costs = int(input("Please input your costs, rub: "))

income = proceeds - costs

if proceeds > costs:
    print(f"Your income = {income}, you are doing great!")
    number_of_staff = int(input("Please input number of staff: "))
    income_to_staff = round(income / number_of_staff, 2)
    print(f"Your income for one person is {income_to_staff} rub.")
else:
    print(f"Your income = {income}, your scores are not very good!")
